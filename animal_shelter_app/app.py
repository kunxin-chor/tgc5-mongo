from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = "animal_shelter"

# Creates a mongo client
client = pymongo.MongoClient(MONGO_URI)

app = Flask(__name__)


@app.route('/show_animals')
def show_animals():
    all_animals = client[DB_NAME].animals.find()
    return render_template('show_animals.template.html', results=all_animals)


@app.route('/create_animal')
def show_create_animal_form():
    return render_template('create_animal.template.html')


@app.route('/create_animal', methods=['POST'])
def process_create_animal():
    # mongo shell uses insert, pymongo uses insert_one
    client.animal_shelter.animals.insert_one({
        "name": request.form.get("animal_name"),
        "breed": request.form.get("animal_breed")
    })
    return "added"


@app.route('/edit_animal/<animal_id>')
def show_edit_animal(animal_id):
    # we use find_one() when we just want one result
    animal = client[DB_NAME].animals.find_one({
        "_id": ObjectId(animal_id)
    })

    """ 
    BIG REMIDNER -- Not all animals have checkups, so you must check if it exists first
    if animal.checkups:
        # if checkups then do something
    """

    return render_template('edit_animal.template.html', animal=animal)


@app.route('/edit_animal/<animal_id>', methods=["POST"])
def process_edit_animal(animal_id):

    client[DB_NAME].animals.update_one({
        "_id": ObjectId(animal_id)
    }, {
        "$set":{
            "name": request.form.get('animal_name'),
            "breed": request.form.get("animal_breed")
        }
    })
    return redirect(url_for("show_animals"))


@app.route('/checkups/<animal_id>')
def show_checkups_for_animal(animal_id):
    animal = client[DB_NAME].animals.find_one({
        "_id": ObjectId(animal_id),
    }, {
        'name': 1, 'checkups': 1
    })

    return render_template('show_checkups.template.html', animal=animal)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
