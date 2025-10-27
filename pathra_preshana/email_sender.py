"""
Email sending functionality using Gmail SMTP
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict


class EmailSender:
    """Class to handle email sending via Gmail"""
    
    def __init__(self, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = os.getenv("GMAIL_USER")
        self.sender_password = os.getenv("GMAIL_APP_PASSWORD")
        
        if not self.sender_email or not self.sender_password:
            raise ValueError("GMAIL_USER and GMAIL_APP_PASSWORD must be set in environment variables")
    
    def send_email(self, recipient_email: str, recipient_name: str, subject: str, html_content: str) -> bool:
        """
        Send an email to a single recipient
        
        Args:
            recipient_email: Email address of recipient
            recipient_name: Name of recipient
            subject: Email subject line
            html_content: HTML formatted email content
            
        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = recipient_email
            
            # Create HTML message
            html_message = MIMEText(html_content, "html")
            message.attach(html_message)
            
            # Send email via SMTP
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            print(f"✓ Email sent successfully to {recipient_name} ({recipient_email})")
            return True
            
        except Exception as e:
            print(f"✗ Failed to send email to {recipient_name} ({recipient_email}): {str(e)}")
            return False
    
    def send_bulk_emails(self, recipients: List[Dict[str, str]], subject: str, html_template: str) -> Dict[str, int]:
        """
        Send emails to multiple recipients
        
        Args:
            recipients: List of dictionaries with 'email' and 'name' keys
            subject: Email subject line
            html_template: HTML template with {name} placeholder
            
        Returns:
            Dictionary with 'success' and 'failed' counts
        """
        results = {"success": 0, "failed": 0}
        
        for recipient in recipients:
            # Replace {name} placeholder with actual name
            personalized_content = html_template.replace("{name}", recipient.get("name", ""))
            
            if self.send_email(
                recipient_email=recipient["email"],
                recipient_name=recipient["name"],
                subject=subject,
                html_content=personalized_content
            ):
                results["success"] += 1
            else:
                results["failed"] += 1
        
        return results

