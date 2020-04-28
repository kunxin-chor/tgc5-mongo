from flask import Flask, render_template, request, redirect, url_for
import os
import datetime
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = "animal_shelter"

# Creates a mongo client
client = pymongo.MongoClient(MONGO_URI)

app = Flask(__name__)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
