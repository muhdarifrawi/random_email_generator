from flask import Flask, render_template, request, url_for, make_response
import random
from io import BytesIO as StringIO
import csv

app = Flask(__name__)

class info:
    email_collection = []
    name_collection= []

@app.route('/')
def main_page():

    download = request.args.get("download")

    if download == "true":

        info.email_collection.insert(0, "email")
        info.name_collection.insert(0, "name")
        si = StringIO()
        cw = csv.writer(si, quoting=csv.QUOTE_NONNUMERIC)
        rows = zip(info.email_collection, info.name_collection)
        for each in rows:
            cw.writerow(each)
        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "text/csv"
        
        return output
    
    return render_template("index.html")

@app.route('/', methods=["POST"])
def generate_email():
    number_of_emails = int(request.form["number"])
    
    animals = ["antelope", "bat", "cat", "dog", "elephant", "fox", "giraffe", "hippopotamus", "impala",
            "jaguar", "kangaroo", "lemur", "monkey", "narwhal", "ostrich", "panda", "quail", "rooster", "snake",
            "tortoise",
            "urchin", "vulture", "whale", "xeme", "yak", "zebra"]

    fruits = ["apple", "banana", "ciku", "durian", "elderberry", "fig", "grape", "huckleberry", "ice-apple", "jackfruit",
            "kiwi", "lime", "melon", "orange", "pumpkin", "quince", "raspberry", "strawberry", "tangerine", "ugli",
            "voavanga",
            "watermelon", "yam", "zuchinni"]

    animal = random.choice(animals)
    fruit = random.choice(fruits)
    email = str(animal) + str(fruit) + "@asd.com"

    counter = 0
    
    if (number_of_emails>0 and number_of_emails < 1000):
       
        #error resolved
        if len(info.email_collection) != 0:
            del info.email_collection[:]
            del info.name_collection[:]

        while counter < number_of_emails:
            animal = random.choice(animals)
            fruit = random.choice(fruits)
            email = str(animal) + str(fruit) + "@asd.com"
            name = str(animal) + " " + str(fruit)
            info.name_collection.append(name)
            info.email_collection.append(email)
            counter += 1

        return render_template("index.html", numberOfEmails=info.email_collection, numberOfNames=info.name_collection, isGenerated=True)
    
    else:
        
        return render_template("index.html", numberOfEmails="Enter a number between 1 to 999.")

    