"""
Google OAuth authentication module
"""

import os
from flask import session, redirect, url_for, request
from functools import wraps
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from google.auth.exceptions import GoogleAuthError

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')


def login_required(f):
    """Decorator to require login for protected routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def verify_google_token(token):
    """
    Verify Google ID token and return user info
    
    Args:
        token: Google ID token from client
        
    Returns:
        dict: User information (email, name, picture, etc.)
    """
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(
            token,
            google_requests.Request(),
            GOOGLE_CLIENT_ID
        )
        
        return {
            'email': idinfo['email'],
            'name': idinfo.get('name', ''),
            'picture': idinfo.get('picture', ''),
            'sub': idinfo['sub']
        }
    except GoogleAuthError as e:
        print(f"Token verification failed: {e}")
        return None


def init_auth(app):
    """Initialize authentication for Flask app"""
    app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))
    
    @app.route('/login')
    def login():
        """Login page"""
        next_url = request.args.get('next', '/')
        return redirect(url_for('static', filename='login.html', next=next_url))
    
    @app.route('/logout')
    def logout():
        """Logout and clear session"""
        session.clear()
        return redirect(url_for('index'))


def is_authenticated():
    """Check if user is authenticated"""
    return 'user_email' in session


def get_current_user():
    """Get current user info from session"""
    if not is_authenticated():
        return None
    
    return {
        'email': session.get('user_email'),
        'name': session.get('user_name'),
        'picture': session.get('user_picture')
    }

