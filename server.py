'''the csv and flask file are for files and website respectively'''
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def my_home():
    '''function walks so that the user gets to the home page on visitation to the site'''
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    '''this function is to render the template of the index.html file'''
    return render_template(page_name)

def write_to_file(data):
    '''this particular python function ensures that the data to the CSV file is received'''
    with open('database.txt', mode='a', encoding='UTF-8') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    '''this function write the available data into a CSV file'''
    with open('database.csv', newline='', mode='a', encoding='UTF-8') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    '''ensures that submitted data in CSV file is redirected to the thankyou html file'''
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')

        except FileNotFoundError:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


if __name__ == '__name__':
    app.run(debug=True, host='0.0.0.0')
