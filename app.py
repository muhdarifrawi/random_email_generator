from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/')
def main_page():
    
    return render_template("index.html")

@app.route('/', methods=["POST"])
def generate_email():
    number_of_emails = request.form["number"]
    
    animals = ["antelope", "bat", "cat", "dog", "elephant", "fox", "giraffe", "hippopotamus", "impala",
            "jaguar", "kangaroo", "lemur", "monkey", "narwhal", "ostrich", "panda", "quail", "rooster", "snake",
            "tortoise",
            "urchin", "vulture", "whale", "xeme", "yak", "zebra"]

    fruits = ["apple", "banana", "ciku", "durian", "elderberry", "fig", "grape", "huckleberry", "ice apple", "jackfruit",
            "kiwi", "lime", "melon", "orange", "pumpkin", "quince", "raspberry", "strawberry", "tangerine", "ugli",
            "voavanga",
            "watermelon", "yam", "zuchinni"]

    animal = random.choice(animals)
    fruit = random.choice(fruits)
    email = str(animal) + str(fruit) + "@asd.com"

    counter = 0
    email_collection = []
    

    # print(email_collection)
    # print(len(email_collection))

    
    if (number_of_emails>0 and number_of_emails < 1000):
        
        while counter < number_of_emails:
            animal = random.choice(animals)
            fruit = random.choice(fruits)
            email = str(animal) + str(fruit) + "@asd.com"
            email_collection.append(email)
            counter += 1

        return render_template("index.html", numberOfEmails=email_collection)
    
    else:
        
        return render_template("index.html", numberOfEmails="Enter a number between 1 to 999.")