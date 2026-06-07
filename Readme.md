# ✉️ MAILCRAFT AI — Intelligent Email Generation Platform

MAILCRAFT AI is a professional multi-page email generation platform built using Streamlit and Google Gemini. It enables users to generate, edit, personalize, and send professional emails with attachment support and multi-recipient functionality.

---

## Project Structure

```
Smart Email Pro/

├── app.py

├── .env

├── smart_email_generator.py

├── data/

│   └── history.json

├── pages/

│   ├── compose.py

│   ├── receiver.py

│   ├── history.py

│   └── settings.py

├── services/

│   └── attachment_handler.py

├── utils/

│   ├── auth.py

│   ├── email_sender.py

│   ├── styles.py

│   └── history_manager.py

├── requirements.txt

└── README.md
```

---

# Features

### AI Email Generation

Generate complete emails automatically using Google Gemini by simply describing the purpose.

### Tone Selection

Supports multiple writing styles:

* Professional
* Friendly
* Formal
* Casual
* Persuasive

### Automatic Subject Generation

Subjects are generated automatically and remain editable before sending.

### Multi Recipient Support

Send emails to multiple receivers simultaneously.

### Attachment Support

Supports:

* Documents
* Images
* PDFs
* Multiple file uploads

### Gmail Authentication

Login using:

* Gmail Address
* Google App Password

Optional password remembering functionality included.

### Email History

Automatically stores:

* Receiver Emails
* Subject
* Body
* Date & Time

### Editable Emails

Users can modify:

* Subject
* Email Body

before sending.

---

# Installation

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create Environment File

Create:

```
.env
```

Add:

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Gmail Setup

To send emails:

### Step 1

Open:

```
Google Account

↓

Security
```

### Step 2

Enable:

```
2 Step Verification
```

### Step 3

Open:

```
App Passwords
```

### Step 4

Generate:

```
Mail App Password
```

### Step 5

Paste password inside MAILCRAFT AI login screen.

---

# Technology Stack

* Python
* Streamlit
* Google Gemini API
* SMTP
* JSON Storage

---

# Workflow

```
Login

↓

Compose Email

↓

Generate Email

↓

Edit Email

↓

Add Attachments

↓

Select Receivers

↓

Send Email

↓

Store History
```
