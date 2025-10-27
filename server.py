from flask import Flask, render_template, request, redirect, flash, send_from_directory, abort, Response
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import re

app = Flask(__name__)

# Load environment variables and secret keys
load_dotenv()
app.secret_key = os.getenv('APP_SECRET_KEY')

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

# ---- Resume download config ----
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Accept common possibilities; your file is called "My_CV"
CANDIDATE_NAMES = ["My_CV.pdf", "My_CV.PDF", "My_CV.docx", "My_CV", "My_CV.doc"]
DOWNLOAD_NAME = "Kehinde_Adekola_CV.pdf"  # what the user sees on download

def find_cv_filename():
    """Return the actual filename of the CV in BASE_DIR or None."""
    for name in CANDIDATE_NAMES:
        candidate = os.path.join(BASE_DIR, name)
        if os.path.isfile(candidate):
            print(f"[server] Using CV file: {os.path.basename(candidate)}")  # debug
            return os.path.basename(candidate)
    print("[server] No CV file found in BASE_DIR")
    return None


@app.route('/resume-pdf')
def resume_pdf():
    cv_file = find_cv_filename()
    if not cv_file or not cv_file.lower().endswith('.pdf'):
        return render_template('not-found.html'), 404

    resp = send_from_directory(
        BASE_DIR,
        cv_file,
        as_attachment=False,
        mimetype='application/pdf',
        download_name=DOWNLOAD_NAME
    )
    # discourage caching the inline preview
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    return resp

@app.route('/download-cv')
def download_cv():
    cv_file = find_cv_filename()
    if not cv_file:
        return render_template('not-found.html'), 404

    return send_from_directory(
        BASE_DIR,
        cv_file,
        as_attachment=True,
        download_name=DOWNLOAD_NAME
    )

@app.route('/')
def my_home():
    """Render the home template"""
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    """Dynamically render any page name"""
    return render_template(page_name)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """Handle form submission"""
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        # Validate email
        email_validation_result = validate_email(email)
        if email_validation_result is not None:
            flash(email_validation_result, 'error')
            return render_template('contact.html', data=data)

        try:
            send_email(email, subject, message)
            return redirect('/thankyou.html')
        except Exception as e:
            print(f"Error: {e}")
            flash('Something went wrong while sending the email. Please try again.', 'error')
            return redirect('/contact.html')

def validate_email(user_email):
    """Validate user email"""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    email_domains = [
        'gmail.com','yahoo.com','outlook.com','protonmail.com',
        'icloud.com','zoho.com','aol.com','yandex.com'
    ]

    if not user_email:
        return 'Email is required'

    if re.match(email_regex, user_email):
        domain = user_email.split('@')[-1]
        if domain in email_domains:
            return None
        else:
            return 'This email domain is not accepted'
    return 'Invalid email format'

def send_email(email, subject, message):
    """Send email to myself"""
    msg = Message(
        subject=f"New Portfolio Message From {email}",
        sender=os.getenv('MAIL_USERNAME'),
        recipients=[os.getenv('MAIL_USERNAME')]
    )
    msg.body = f"Subject: {subject}\n\nMessage: {message}\n\nFrom: {email}"
    mail.send(msg)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('not-found.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
