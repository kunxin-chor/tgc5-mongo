import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = "notecards"
client = None


def get_client():
    global client
    if client is None:
        client = pymongo.MongoClient(MONGO_URI)
    return client


def get_db():
    client = get_client()
    return client[DB_NAME]


def get_notecards(tags=[]):
    filter = {}

    # include in tags
    if len(tags) > 0:
        filter['tags'] = {
            '$in': tags
        }

    conn = get_db()
    return conn["notes"].find(filter)


def insert_notecard(title, content, tags):
    conn = get_db()
    conn["notes"].insert_one({
        "title": title,
        "content": content,
        "tags": tags
    })
