from flask import Flask, render_template, request, redirect, flash
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

@app.route('/')
def my_home():
    '''Render the home template'''
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    '''Dynamically render any page name'''
    return render_template(page_name)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    '''Handle form submission'''
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
    '''Validate user email'''
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    email_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com', 'icloud.com', 'zoho.com', 'aol.com', 'yandex.com']

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
    '''Send email to myself'''
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
