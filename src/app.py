import os
from dotenv import load_dotenv
from email_utils import send_email_gmail

_ = load_dotenv('../.env',override=True)

if __name__ == "__main__":
    # Replace with your details
    sender = os.environ.get('GMAIL_USER')
    app_password = os.environ.get('GMAIL_PASSWORD')
    recipient = os.environ.get('EMAIL_RECIPIENT')
    subject = "Test Email from Python"
    body = "Hello! This is a test email sent from Python using Gmail SMTP."

    send_email_gmail(sender, app_password, recipient, subject, body)