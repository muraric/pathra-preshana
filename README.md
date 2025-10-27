# Pathra Preshana

Automated Email Sending System using Gmail

## Features

✅ Send personalized HTML emails to multiple recipients  
✅ Read email recipients from CSV file  
✅ Customize email content with HTML templates  
✅ Dynamic name replacement in email content  
✅ Environment-based configuration for Gmail credentials  

## Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Gmail App Password

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification**
3. Scroll down to **App passwords**
4. Generate a new app password for "Mail"
5. Copy the 16-character password

### 3. Configure Environment Variables

Copy the example environment file and update with your credentials:

```bash
cp .env.example .env
```

Edit `.env` and add your Gmail credentials:

```
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_16_char_app_password
```

### 4. Prepare Your Email Content

**HTML Template:**
- Place your HTML email template in `templates/email_template.html`
- Use `{name}` placeholder to insert recipient names dynamically
- The template includes both HTML structure and CSS styling

**Recipients CSV:**
- Update `data/recipients.csv` with your recipient list
- Required format: `name,email`
- Example:
  ```
  name,email
  John Doe,john@example.com
  Jane Smith,jane@example.com
  ```

## Usage

Run the application:

```bash
python -m pathra_preshana.main
```

The application will prompt you for:
- Path to HTML template (or use default: `templates/email_template.html`)
- Path to CSV file (or use default: `data/recipients.csv`)
- Email subject line

## Project Structure

```
pathra-preshana/
├── pathra_preshana/
│   ├── __init__.py
│   ├── main.py              # Main entry point
│   ├── email_sender.py      # Gmail SMTP email sending
│   └── file_reader.py       # HTML and CSV file reading
├── templates/
│   └── email_template.html  # Email HTML template
├── data/
│   └── recipients.csv       # Email recipients list
├── .env                     # Environment variables (create from .env.example)
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## How It Works

1. **Read HTML Template**: Loads the HTML email template from specified file
2. **Read Recipients**: Parses CSV file to extract email addresses and names
3. **Personalize Content**: Replaces `{name}` placeholder with actual recipient name
4. **Send Emails**: Sends personalized emails via Gmail SMTP
5. **Summary Report**: Shows success/failure count

## CSV Format

The recipients CSV file must have at least an `email` column. A `name` column is optional.

```csv
name,email
John Doe,john@example.com
Jane Smith,jane@example.com
```

## Customization

### HTML Template

Create your own HTML email template:
- Place it in `templates/` directory
- Use `{name}` placeholder for personalization
- Include inline CSS for styling
- Support responsive design for mobile devices

### Email Content

You can customize:
- Email subject line
- HTML template content
- CSS styling
- Recipient list

## Troubleshooting

**"Gmail authentication failed"**
- Verify your Gmail app password is correct
- Make sure 2-Step Verification is enabled
- Check that `.env` file has correct credentials

**"File not found"**
- Ensure template and CSV files exist at specified paths
- Use absolute paths or paths relative to project root

**"No recipients found"**
- Verify CSV file has `email` column
- Check that emails are not empty
- Ensure CSV file is properly formatted

## Security Notes

- Never commit `.env` file to version control
- Use app passwords, not your main Gmail password
- Keep your app password secure
- The `.env` file is already in `.gitignore`
