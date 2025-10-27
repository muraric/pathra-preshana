"""
Flask web application for Pathra Preshana email sender
"""

import os
from flask import Flask, render_template, request, jsonify, send_file, session, redirect, url_for
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from pathra_preshana.email_sender import EmailSender
from pathra_preshana.file_reader import FileReader
from pathra_preshana.auth import (
    login_required, 
    verify_google_token, 
    init_auth as init_auth_module,
    is_authenticated,
    get_current_user
)

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize authentication
init_auth_module(app)

ALLOWED_EXTENSIONS = {'html', 'csv'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_template_files():
    """Get list of HTML templates in templates directory"""
    templates_dir = 'templates'
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
    
    files = [f for f in os.listdir(templates_dir) if f.endswith('.html')]
    return files


def get_recipient_files():
    """Get list of CSV files in data directory"""
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    return files


@app.route('/')
def index():
    """Main page with UI"""
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    return render_template('web_ui.html', user=user)


@app.route('/api/templates')
def get_templates():
    """Get list of available templates"""
    templates = get_template_files()
    return jsonify({'templates': templates})


@app.route('/api/recipients')
def get_recipients():
    """Get list of available recipient files"""
    recipients = get_recipient_files()
    return jsonify({'recipients': recipients})


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file uploads for templates and recipients"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    file_type = request.form.get('type')  # 'template' or 'recipients'
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Determine destination directory
        if file_type == 'template':
            if not filename.endswith('.html'):
                return jsonify({'error': 'Template must be a .html file'}), 400
            upload_dir = 'templates'
        elif file_type == 'recipients':
            if not filename.endswith('.csv'):
                return jsonify({'error': 'Recipients file must be a .csv file'}), 400
            upload_dir = 'data'
        else:
            return jsonify({'error': 'Invalid file type specified'}), 400
        
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)
        
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'type': file_type
        })
    
    return jsonify({'error': 'Invalid file type'}), 400


@app.route('/api/preview', methods=['POST'])
def preview_template():
    """Preview HTML template with sample data"""
    data = request.json
    template_path = data.get('template_path')
    
    if not template_path:
        return jsonify({'error': 'Template path required'}), 400
    
    try:
        file_reader = FileReader()
        html_content = file_reader.read_html_template(template_path)
        
        # Replace {name} with sample data
        preview_content = html_content.replace('{name}', 'John Doe')
        
        return jsonify({'html': preview_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/recipients-data', methods=['POST'])
def get_recipients_data():
    """Get recipients data from CSV file"""
    data = request.json
    csv_path = data.get('csv_path')
    
    if not csv_path:
        return jsonify({'error': 'CSV path required'}), 400
    
    try:
        file_reader = FileReader()
        recipients = file_reader.read_csv_recipients(csv_path)
        
        return jsonify({
            'recipients': recipients,
            'count': len(recipients)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/login')
def login():
    """Login page"""
    client_id = os.getenv('GOOGLE_CLIENT_ID', '')
    return render_template('login.html', google_client_id=client_id)

@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

@app.route('/api/auth/google', methods=['GET', 'POST'])
def google_auth():
    """Handle Google OAuth authentication"""
    if request.method == 'GET':
        # This will be handled by client-side Google Sign-In
        # Return the page that handles Google authentication
        return redirect('/login')

@app.route('/api/auth/google/callback', methods=['POST'])
def google_auth_callback():
    """Handle Google OAuth callback"""
    try:
        data = request.json
        token = data.get('credential')  # Google ID token
        
        if not token:
            return jsonify({'error': 'No credential provided'}), 400
        
        # Verify the Google token
        user_info = verify_google_token(token)
        
        if user_info:
            # Store user info in session
            session['user_email'] = user_info['email']
            session['user_name'] = user_info['name']
            session['user_picture'] = user_info.get('picture', '')
            
            return jsonify({
                'success': True,
                'user': user_info
            })
        else:
            return jsonify({'error': 'Invalid token'}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/status')
def auth_status():
    """Check authentication status"""
    user = get_current_user()
    return jsonify({
        'authenticated': is_authenticated(),
        'user': user
    })

@app.route('/api/send', methods=['POST'])
@login_required
def send_emails():
    """Send emails to recipients"""
    data = request.json
    template_path = data.get('template_path')
    recipients_path = data.get('recipients_path')
    subject = data.get('subject', '')
    
    if not template_path or not recipients_path:
        return jsonify({'error': 'Template and recipients paths required'}), 400
    
    try:
        # Read template
        file_reader = FileReader()
        html_template = file_reader.read_html_template(template_path)
        
        # Read recipients
        recipients = file_reader.read_csv_recipients(recipients_path)
        
        if not recipients:
            return jsonify({'error': 'No recipients found'}), 400
        
        # Send emails
        email_sender = EmailSender()
        results = email_sender.send_bulk_emails(
            recipients=recipients,
            subject=subject,
            html_template=html_template
        )
        
        return jsonify({
            'success': True,
            'results': results
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Use PORT environment variable if available (for production)
    port = int(os.environ.get('PORT', 5001))
    # Debug should be False in production
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)

