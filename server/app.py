import json
from flask import Flask, redirect, request, url_for, session
from flask_pymongo import pymongo
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_cors import CORS
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv
import helpers.utils as utils
import classes.User as User
import validators
import os
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')
login_manager = LoginManager()

CORS(app)
login_manager.init_app(app)
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = os.getenv('GOOGLE_DISCOVERY_URL')
USERNAME = os.getenv('MONGO_USERNAME')
PASSWORD = os.getenv('MONGO_PASSWORD')
google_client = WebApplicationClient(GOOGLE_CLIENT_ID)
CONN_STRING = f"mongodb+srv://{USERNAME}:{PASSWORD}@urlcluster.gagwym9.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONN_STRING)
db = client.get_database('URLCluster')
collection = db.get_collection('urls')

@app.route("/api/url", methods=["POST"])
def create_url():
    data = request.json
    user_entered_url = data['url']
    user_entered_name = data['name']
    base_url = url_for('create_url', _external=True)

    if validators.url(user_entered_url): # Must in the form http(s)://<link>
        if utils.validate_name(collection, user_entered_name):
            collection.insert_one(utils.generate_url_insert(user_entered_name, user_entered_url))
        else:
            return {"message": "Name already in use"}, 400 # Should be an error stating the user entered name was already in use
        return utils.generate_return_url(user_entered_name, base_url) # 201 ok stating the link is good to go, should be returning their short link
    else:
        return {"message": "Invalid URL, link must be in the form http:// or https://"}, 400 # Should be an error stating the link was invalid

@app.route("/api/url/<string:url_id>", methods=["GET"])
def redirect_url(url_id):
    result = collection.find_one({"url_id": url_id})
    if result:
        return redirect(result['url'])
    
    return {"message": "Invalid short URL"}, 404

@app.route("/")
def home():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'

@app.route("/login")
def login():
    provider_config = utils.get_google_provider(GOOGLE_DISCOVERY_URL)
    auth_endpoint = provider_config["authorization_endpoint"]
    redirect_url = request.base_url + "/callback"
    print(redirect_url)
    request_uri = google_client.prepare_request_uri(auth_endpoint, redirect_uri=redirect_url, scope=["openid", "email", "profile"])
   
    return redirect(request_uri)

@app.route("/login/callback")
def loginCallback():
    code = request.args.get("code")
    provider_config = utils.get_google_provider(GOOGLE_DISCOVERY_URL)
    token_endpoint = provider_config["token_endpoint"]

    token_url, headers, body = google_client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    google_client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = provider_config["userinfo_endpoint"]
    uri, headers, body = google_client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
    
    user = User.User(unique_id, users_name, users_email, picture, collection)
    if not User.User.get(unique_id,collection):
        User.User.create(unique_id, users_name, users_email, picture, collection)
    
    login_user(user)

    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@login_manager.user_loader
def load_user(user_id):
    return User.User.get(user_id,collection)

# for local testing, need to ensure https for oauth2 to work
if __name__ == "__main__":
    app.run(ssl_context="adhoc")