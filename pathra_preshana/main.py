"""
Main entry point for the automated email sender application
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from pathra_preshana.email_sender import EmailSender
from pathra_preshana.file_reader import FileReader


def main():
    """Main function to run the email automation"""
    
    # Load environment variables from .env file
    load_dotenv()
    
    print("=" * 60)
    print("Automated Email Sender")
    print("=" * 60)
    print()
    
    # Check if environment variables are set
    if not os.getenv("GMAIL_USER") or not os.getenv("GMAIL_APP_PASSWORD"):
        print("✗ Error: GMAIL_USER and GMAIL_APP_PASSWORD must be set in .env file")
        print("\nPlease create a .env file with the following variables:")
        print("GMAIL_USER=your_email@gmail.com")
        print("GMAIL_APP_PASSWORD=your_app_password")
        return 1
    
    # Prompt for file paths
    print("File Configuration:")
    print("-" * 60)
    
    html_template_path = input("Enter path to HTML email template (or press Enter for default: templates/email_template.html): ").strip()
    if not html_template_path:
        html_template_path = "templates/email_template.html"
    
    csv_file_path = input("Enter path to CSV file with recipients (or press Enter for default: data/recipients.csv): ").strip()
    if not csv_file_path:
        csv_file_path = "data/recipients.csv"
    
    email_subject = input("Enter email subject: ").strip()
    if not email_subject:
        email_subject = "Hello from Pathra Preshana"
    
    print()
    print("=" * 60)
    print("Sending Emails...")
    print("=" * 60)
    print()
    
    try:
        # Read HTML template
        file_reader = FileReader()
        html_template = file_reader.read_html_template(html_template_path)
        
        # Read CSV recipients
        recipients = file_reader.read_csv_recipients(csv_file_path)
        
        if not recipients:
            print("✗ No recipients found in CSV file")
            return 1
        
        # Initialize email sender
        email_sender = EmailSender()
        
        # Send emails
        results = email_sender.send_bulk_emails(
            recipients=recipients,
            subject=email_subject,
            html_template=html_template
        )
        
        # Print summary
        print()
        print("=" * 60)
        print("Email Summary")
        print("=" * 60)
        print(f"Total Recipients: {len(recipients)}")
        print(f"✓ Successfully Sent: {results['success']}")
        print(f"✗ Failed: {results['failed']}")
        print("=" * 60)
        
        return 0 if results['failed'] == 0 else 1
        
    except FileNotFoundError as e:
        print(f"✗ Error: File not found - {str(e)}")
        return 1
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
