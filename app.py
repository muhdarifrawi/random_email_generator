from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def generate_email():
    number_of_emails = int(request.form["number"])
    
    if (number_of_emails>0 and number_of_emails < 1000):
        print("here", number_of_emails)

        return render_template("index.html", numberOfEmails=number_of_emails)
    
    else:
        print("there", number_of_emails)
        return render_template("index.html", numberOfEmails="Enter a number between 1 to 999.")