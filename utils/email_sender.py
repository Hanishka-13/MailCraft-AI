import smtplib
import json
import os
from datetime import datetime
from email.message import EmailMessage
def send_email(receiver,subject,body,attachments,sender,password):
    msg=EmailMessage()
    msg["From"]=sender
    msg["To"]=receiver
    msg["Subject"]=subject
    msg.set_content(body)
    # ATTACHMENTS
    for file in attachments:
        msg.add_attachment(
            file["content"],
            maintype=file["maintype"],
            subtype=file["subtype"],
            filename=file["filename"]
        )
    # SEND MAIL
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender,password)
    server.send_message(msg)
    server.quit()
    # SAVE HISTORY
    history_folder="data"
    history_file="data/history.json"
    if not os.path.exists(history_folder):
        os.makedirs(history_folder)
    history=[]
    if os.path.exists(history_file):
        try:
            with open(history_file,"r",encoding="utf-8") as f:
                history=json.load(f)
        except:
            history=[]
    history.append(
        {
            "receiver":receiver,
            "subject":subject,
            "body":body,
            "time":datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            )
        }
    )
    with open(history_file,"w",encoding="utf-8") as f:
        json.dump(history, f, indent=4)