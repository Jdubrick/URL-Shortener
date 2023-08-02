from flask import Flask, redirect, request
from flask_pymongo import pymongo
from flask_cors import CORS
from dotenv import load_dotenv
import helpers.utils as utils
import validators
import os

load_dotenv()
app = Flask(__name__)
CORS(app)
USERNAME = os.getenv('MONGO_USERNAME')
PASSWORD = os.getenv('MONGO_PASSWORD')
CONN_STRING = f"mongodb+srv://{USERNAME}:{PASSWORD}@urlcluster.gagwym9.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONN_STRING)
db = client.get_database('URLCluster')
collection = db.get_collection('urls')

@app.route("/api/url", methods=["POST"])
def create_url():
    data = request.json
    user_entered_url = data['url']
    user_entered_name = data['name']
    if validators.url(user_entered_url): # Must in the form http(s)://<link>
        if utils.validate_name(collection, user_entered_name):
            collection.insert_one(utils.generate_url_insert(user_entered_name, user_entered_url))
        else:
            return {"message": "Name already in use"}, 400 # Should be an error stating the user entered name was already in use
        return utils.generate_return_url(user_entered_name) # 201 ok stating the link is good to go, should be returning their short link
    else:
        return {"message": "Invalid URL, link must be in the form http:// or https://"}, 400 # Should be an error stating the link was invalid

@app.route("/api/url/<string:url_id>", methods=["GET"])
def redirect_url(url_id):
    result = collection.find_one({"url_id": url_id})
    if result:
        return redirect(result['url'])
    
    return {"message": "Invalid short URL"}, 404

