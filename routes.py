# routes.py
"""
Route definitions for the Flask app.
All routes and error handlers.
"""

from flask import render_template, request, redirect, flash, send_from_directory
from config import DOWNLOAD_NAME, BASE_DIR
from utils import find_cv_filename, validate_email, send_email

def register_routes(app, mail):
    """Register all routes and error handlers on the app."""

    @app.route('/')
    def my_home():
        """Render the home template."""
        return render_template('index.html')

    @app.route('/<string:page_name>')
    def html_page(page_name):
        """Dynamically render any page name."""
        return render_template(page_name)

    @app.route('/submit_form', methods=['POST'])
    def submit_form():
        """Handle form submission."""
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
                send_email(mail, email, subject, message)
                return redirect('/thankyou.html')
            except Exception as e:
                print(f"Error: {e}")
                flash('Something went wrong while sending the email. Please try again.', 'error')
                return redirect('/contact.html')

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
        # Cache headers
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        resp.headers["Pragma"] = "no-cache"
        # iframe/PDF compatibility
        resp.headers["X-Frame-Options"] = "SAMEORIGIN"
        resp.headers["Content-Disposition"] = f"inline; filename={DOWNLOAD_NAME}"
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

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('not-found.html'), 404