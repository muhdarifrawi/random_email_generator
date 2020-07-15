from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def generate_email():
    number_of_emails = request.form["number"]

    return render_template("index.html", numberOfEmails=number_of_emails)