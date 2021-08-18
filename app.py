from flask import Flask, render_template, url_for, request, redirect
import csv
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("./index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
 with open('database.csv', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar=';',quoting= csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])


def email_sender(data):
    email = EmailMessage()
    email['from'] = data["email"]
    email['to'] = 'danieldamilola05@gmail.com'
    email['subject'] = data["subject"]

    email.set_content(data['message'])

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('alphadan0005@gmail.com', 'Danbell05')
        smtp.submit_form()



@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        email_sender(data)
        return redirect("./thanks.html")
    else:
        return "Something went wrong"
