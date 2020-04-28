from flask import Flask, render_template, request, redirect, url_for
import os
import math
import datetime
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = "sample_airbnb"

# Creates a mongo client
client = pymongo.MongoClient(MONGO_URI)

app = Flask(__name__)


@app.route('/')
def index():

    records_per_page = 10
    max_pages = math.ceil(client[DB_NAME]['listingsAndReviews'].count() / records_per_page)

    current_page = int(request.args.get('current_page', 1))


    # only show the first ten
    listings = client[DB_NAME]['listingsAndReviews'].find({}).skip((current_page-1)*records_per_page).limit(records_per_page)
    return render_template('index.template.html', results=listings, max_pages=max_pages, current_page=current_page)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
