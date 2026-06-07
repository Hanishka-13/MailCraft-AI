"""Email generation using Google Gemini."""
import re
import time
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
# GEMINI CONFIG
client = os.getenv("API_KEY")
# GENERATE EMAIL
def generate_email(purpose:str,tone:str="Professional",extra_context:str="")->dict:
    prompt=f"""
        You are an expert professional email writer.
        Write a complete email.
        Tone:
        {tone}
        Purpose:
        {purpose}
        {f"Extra Context: {extra_context}" if extra_context else ""}
        Instructions:
        - Create professional subject automatically
        - Write complete email
        - Include greeting
        - Explain purpose clearly
        - Include important details
        - Include action request
        - End professionally
        - Use placeholders ONLY if needed:
        [RECIPIENT_NAME]
        [COMPANY]
        [DATE]
        [YOUR_NAME]
        Do NOT use markdown.
        Output ONLY:
        SUBJECT: <subject>
        BODY:
        <email body>
        """
    response=None
    for attempt in range(3):
        try:
            response=client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            break
        except Exception as e:
            error=str(e)
            # QUOTA EXCEEDED
            if ("429" in error or "RESOURCE_EXHAUSTED" in error):
                return _fallback_email(purpose)
            # SERVER BUSY
            if ("503" in error or "UNAVAILABLE" in error):
                time.sleep(3)
                continue
            return {
                "subject":"Generation Failed",
                "body":error
            }
    if response is None:
        return _fallback_email(purpose)
    return _parse_email_response(response.text)

# PARSE RESPONSE
def _parse_email_response(text:str)->dict:
    subject="Professional Email"
    body=text
    body_started=False
    collected=[]
    lines=text.split("\n")
    for line in lines:
        stripped=line.strip()
        if stripped.upper().startswith("SUBJECT:"):
            subject=stripped.replace("SUBJECT:","").strip()
            continue
        if stripped.upper().startswith("BODY:"):
            body_started=True
            continue
        if body_started:
            collected.append(line)
    if collected:
        body="\n".join(collected).strip()
    subject=re.sub(r"\[[^\]]+\]","",subject).strip()
    if not subject:
        subject="Professional Email"
    return {
        "subject":subject,
        "body":body
    }

# FALLBACK EMAIL
def _fallback_email(purpose:str)->dict:
    return {
        "subject":purpose.title(),
        "body":f"""
        Dear [RECIPIENT_NAME],
        I hope you are doing well.
        I am writing regarding:
        {purpose}
        Please let me know if any additional information is required.
        Thank you.
        Best Regards,
        [YOUR_NAME]
        """
    }

# PLACEHOLDERS
def extract_placeholders(text:str)->list:
    return list(
        dict.fromkeys(
            re.findall(r'\[([^\[\]]+)\]',text)
        )
    )
def fill_placeholders(text:str,values:dict)->str:
    for key,val in values.items():
        if val and str(val).strip():
            text=text.replace(f"[{key}]",str(val).strip())
    return text