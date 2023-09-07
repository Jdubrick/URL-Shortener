from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, email, profile_img, collection) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.profile_img = profile_img
        self.collection = collection

    @staticmethod
    def get(user_email, db_collection):
        result = db_collection.find_one({"user_email": user_email})
        if not result:
            return None
        
        user = User(result['user_id'], result['user_name'], result['user_email'], result['user_profile_img'])

        return user
    
    @staticmethod
    def create(id, name, email, profile_img, db_collection):
        db_collection.insert_one({"user_id": id, "user_email": email, "user_name": name, "user_profile_img": profile_img})
