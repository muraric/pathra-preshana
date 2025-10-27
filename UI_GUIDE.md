# Pathra Preshana - Web UI Guide

## 🎉 Feature Complete!

The web UI has been successfully implemented with all requested features.

## ✨ Features Implemented

1. ✅ **Upload HTML Templates** - Drag & drop or click to upload HTML email templates
2. ✅ **Upload Recipients File** - Drag & drop or click to upload CSV files with recipient data
3. ✅ **Template Dropdown** - Select from available HTML templates
4. ✅ **Recipients Dropdown** - Select from available CSV recipient files
5. ✅ **Preview HTML Template** - Preview the email with sample data before sending
6. ✅ **Send Mail Button** - Send personalized emails to all recipients

## 🚀 How to Run

### Option 1: Using the run script
```bash
source venv/bin/activate
python run_ui.py
```

### Option 2: Using Flask directly
```bash
source venv/bin/activate
python -m pathra_preshana.app
```

### Option 3: Using the background server
The server is already running in the background! Just access it at:
```
http://localhost:5001
```

## 📱 Using the Web UI

1. **Upload Files**
   - Click on the upload areas to upload new templates or recipient files
   - Supported formats: `.html` for templates, `.csv` for recipients

2. **Select Configuration**
   - Choose a template from the dropdown
   - Choose a recipients CSV file
   - Enter an email subject

3. **Preview**
   - Click "Preview" to see how the email will look
   - Uses "John Doe" as sample data

4. **Send Emails**
   - Click "Send Emails" to send personalized emails
   - You'll see a confirmation dialog first
   - Results will show success/failure counts

## 📁 File Structure

```
pathra-preshana/
├── pathra_preshana/
│   ├── app.py              # Flask web application
│   ├── email_sender.py     # Email sending logic
│   ├── file_reader.py      # File reading utilities
│   └── main.py             # CLI version
├── templates/
│   ├── email_template.html # Default email template
│   └── web_ui.html         # Web UI interface
├── data/
│   └── recipients.csv      # Recipient data
├── .env                    # Gmail credentials
├── requirements.txt        # Python dependencies
└── run_ui.py              # Web UI launcher
```

## 🎨 UI Highlights

- **Modern Design** - Beautiful gradient header and clean interface
- **Responsive** - Works on desktop and mobile devices
- **File Upload** - Drag & drop support for easy file management
- **Live Preview** - See your emails before sending
- **Status Messages** - Clear feedback for all operations
- **Confirmation Dialogs** - Prevent accidental email sends

## 🔧 API Endpoints

- `GET /` - Main UI page
- `GET /api/templates` - Get list of templates
- `GET /api/recipients` - Get list of recipient files
- `POST /api/upload` - Upload templates or recipients
- `POST /api/preview` - Preview template with sample data
- `POST /api/recipients-data` - Get recipients from CSV
- `POST /api/send` - Send emails to recipients

## 📝 CSV Format

The recipients CSV file should follow this format:

```csv
name,email
John Doe,john@example.com
Jane Smith,jane@example.com
```

## 🔐 Security

- Uses Gmail App Password for secure authentication
- File size limit: 16MB per upload
- Secure file naming with `secure_filename()`
- Proper validation of file types

## 🐛 Troubleshooting

**Can't access the web UI?**
- Make sure the server is running: `python run_ui.py`
- Check if port 5001 is already in use (port 5000 is used by macOS AirPlay)
- Access: `http://localhost:5001`

**Upload errors?**
- Ensure files are `.html` (templates) or `.csv` (recipients)
- Check file size (max 16MB)

**Email sending fails?**
- Verify `.env` file has correct Gmail credentials
- Ensure 2-Step Verification is enabled in Google Account
- Use App Password, not regular Gmail password

## 🎯 Branch Information

- **Current Branch**: `feature/ui`
- **Status**: ✅ Complete and ready for testing
- **Changes**: Added Flask web UI with file upload and preview capabilities

---

**Note**: The web server runs on port 5001 by default (to avoid conflicts with macOS AirPlay on port 5000). If you need to change this, edit `run_ui.py` or `pathra_preshana/app.py`.

