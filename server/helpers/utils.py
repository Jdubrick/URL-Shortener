import datetime

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
def generate_return_url(user_entered_name):
    return {
        "message": "URL created successfuly",
        "url": f"http://localhost:5000/api/url/{user_entered_name}"
    }, 201