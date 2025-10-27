# Quick Setup Guide

## 1. Install Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Get Gmail App Password

1. Visit: https://myaccount.google.com/apppasswords
2. If 2-Step Verification is not enabled, enable it first
3. Generate app password for "Mail"
4. Copy the 16-character password

## 4. Configure .env File

Edit `.env` file with your Gmail credentials:

```bash
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_16_char_password_here
```

## 5. Customize Your Content

**Edit HTML Template:**
- Open `templates/email_template.html`
- Modify the HTML content and CSS
- Use `{name}` placeholder for personalization

**Edit Recipients:**
- Open `data/recipients.csv`
- Add your email recipients
- Format: `name,email`

## 6. Run the Application

```bash
python -m pathra_preshana.main
```

Follow the prompts to send emails!

## Troubleshooting

**Authentication Failed:**
- Make sure you're using an App Password, not your regular Gmail password
- Verify 2-Step Verification is enabled

**Import Errors:**
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**File Not Found:**
- Use absolute paths or relative paths from project root
- Default files: `templates/email_template.html` and `data/recipients.csv`

