import datetime
import requests

def validate_name(collection, parameter):
    result = collection.find({"url_id": parameter})
    if len(list(result)) != 0:
        return False
    return True

def generate_url_insert(user_entered_name, user_entered_url):
    return {
        "url_id": user_entered_name,
        "url": user_entered_url,
        "timestamp": datetime.datetime.now()
    }

#TODO: make this so its not hardcoded localhost and will take wherever the server is
def generate_return_url(user_entered_name, base_url):
    return {
        "message": "URL created successfuly",
        "url": f"{base_url}/{user_entered_name}"
    }, 201

def get_google_provider(url):
    return requests.get(url).json()