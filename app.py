from flask import Flask, render_template, request, url_for, make_response
import random
from io import BytesIO as StringIO
import csv
# this three lines are for python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()

import pymongo
import csv

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLL = os.getenv("MONGO_COLL")

conn =  pymongo.MongoClient(MONGO_URI)

app = Flask(__name__)

class info:
    email_collection = []
    name_collection = []
    phone_collection = []

def random_phone_generator():
    first_number = random.randint(6,9)
    first_number = str(first_number)
    hp = first_number
    for each in range(7):
        number = random.randint(0,9)
        number = str(number)
        hp = hp + number
    return hp

@app.route('/')
def main_page():

    data = conn[MONGO_DB][MONGO_COLL]
    

    download = request.args.get("download")

    if download == "true":
        data.remove({})

        for each in range(len(info.email_collection)):
            data.insert(
               {
                "name": info.name_collection[each],
                "email":info.email_collection[each],
                "phone_number": info.phone_collection[each]
               }
            )
        with open("test-file","w") as file:
            write_file = csv.writer(file)
            export_data = data.find()
            for each in export_data:
                write_file.writerow([each.name,each.email,each.phone_number])

            output = make_response(StringIO().getvalue())
            output.headers["Content-Disposition"] = "attachment; filename=export.csv"
            output.headers["Content-type"] = "text/csv"
    
    return render_template("index.html",data=data)

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
            del info.phone_collection[:]

        while counter < number_of_emails:
            animal = random.choice(animals)
            fruit = random.choice(fruits)
            email = str(animal) + str(fruit) + "@asd.com"
            name = str(animal) + " " + str(fruit)
            phone = random_phone_generator()
            info.name_collection.append(name)
            info.email_collection.append(email)
            info.phone_collection.append(phone)
            counter += 1

        return render_template("index.html", numberOfEmails=info.email_collection, 
        numberOfNames=info.name_collection, numberOfPhones=info.phone_collection ,isGenerated=True)
    
    else:
        
        return render_template("index.html", numberOfEmails="Enter a number between 1 to 999.")

    