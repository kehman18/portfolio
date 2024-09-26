from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'  # E.g., smtp.gmail.com for Gmail
app.config['MAIL_PORT'] = 465  # Or 587 for TLS
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'kehindeadekola96@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password

mail = Mail(app)

@app.route('/')
def my_home():
    '''function walks so that the user gets to the home page on visitation to the site'''
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    '''this function is to render the template of the index.html file'''
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    '''Ensures that submitted data is emailed to the recipient'''
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            send_email(data)
            return redirect('/thankyou.html')
        except Exception as e:
            print(f"Error: {e}")
            return 'Something went wrong. Please try again later.'
    else:
        return 'Something went wrong. Try again!'

def send_email(data):
    '''This function sends the form data via email'''
    email = data['email']
    subject = data['subject']
    message = data['message']

    # Compose the email
    msg = Message(subject=f"New Portfolio Message From {email}", 
                  sender='your-email@example.com', 
                  recipients=['your-email@example.com'])  # Email where you'd like to receive the messages
    msg.body = f"Subject: {subject}\n\nMessage: {message}\n\nFrom: {email}"

    # Send the email
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
