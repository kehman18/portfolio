# utils.py
"""
Utility functions for the Flask app.
Includes CV file finding and email handling.
"""

import os
import re
from flask_mail import Message
from config import BASE_DIR, CANDIDATE_NAMES, DOWNLOAD_NAME, MAIL_USERNAME, ALLOWED_EMAIL_DOMAINS, EMAIL_REGEX

def find_cv_filename():
    """Return the actual filename of the CV in BASE_DIR or None."""
    for name in CANDIDATE_NAMES:
        candidate = os.path.join(BASE_DIR, name)
        if os.path.isfile(candidate):
            print(f"[server] Using CV file: {os.path.basename(candidate)}")  # debug
            return os.path.basename(candidate)
    print("[server] No CV file found in BASE_DIR")
    return None

def validate_email(user_email):
    """Validate user email format and allowed domain."""
    if not user_email:
        return 'Email is required'

    if re.match(EMAIL_REGEX, user_email):
        domain = user_email.split('@')[-1]
        if domain in ALLOWED_EMAIL_DOMAINS:
            return None
        else:
            return 'This email domain is not accepted'
    return 'Invalid email format'

def send_email(mail_instance, email, subject, message):
    """Send email using the provided Mail instance."""
    msg = Message(
        subject=f"New Portfolio Message From {email}",
        sender=MAIL_USERNAME,
        recipients=[MAIL_USERNAME]
    )
    msg.body = f"Subject: {subject}\n\nMessage: {message}\n\nFrom: {email}"
    mail_instance.send(msg)