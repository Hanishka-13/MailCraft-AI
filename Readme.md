# ✉️ MailCraft AI — Smart Email Generator

A professional multi-page Streamlit app powered by Google Gemini that writes, edits, and sends emails for you.

---

## 🗂️ Project Structure

```
smart_email_pro/
├── Home.py                        ← App entry point (landing page)
├── smart_email_generator.py       ← AI backend (Gemini API)
├── requirements.txt
└── pages/
    ├── 1_✉️_Compose.py            ← AI email composer
    ├── 2_📋_Templates.py          ← Pre-built templates
    ├── 3_📜_History.py            ← Session history
    └── 4_⚙️_Settings.py          ← SMTP + preferences
```

---

## 🚀 Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Gemini API key
Open `smart_email_generator.py` and replace:
```python
api_key="YOUR_GEMINI_API_KEY_HERE"
```
with your actual key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 3. Run the app
```bash
streamlit run Home.py
```

---

## 📄 Pages

| Page | What it does |
|------|-------------|
| 🏠 Home | Landing page with feature overview |
| ✉️ Compose | AI email generator with editing, placeholders, and send |
| 📋 Templates | 10+ pre-built templates (career, business, apology, personal) |
| 📜 History | View, search, reload, or delete past emails |
| ⚙️ Settings | Save Gmail SMTP credentials + default tone preferences |

---

## 🔐 Gmail Setup

To send emails, you need a **Google App Password**:
1. Go to myaccount.google.com → Security
2. Enable 2-Step Verification
3. Search "App passwords" and create one for Mail
4. Paste the 16-character password in Settings or the Compose page

---

## ✨ Features

- **AI Compose** — Describe your email in plain English; Gemini writes it
- **Tone Control** — Professional, Formal, Friendly, Persuasive, Apologetic
- **AI Improve** — Refine your draft with natural language instructions
- **Smart Placeholders** — Auto-detects `[NAME]`, `[COMPANY]`, etc.
- **Templates** — 10+ ready-to-use email templates across categories
- **History** — Every email saved in-session with search and delete
- **One-click Send** — Direct Gmail SMTP integration
- **Saved Settings** — Store credentials once, use across pages