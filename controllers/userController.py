from models.User import User
from config import db

def get_all_user():
    users = User.query.all()
    print(users)
    
    return [user.to_dict() for user in users]

def get_user_by_id(user_id):
    return User.query.get(user_id)
def create_user(data):
   
        user = User(name=data['name'], email=data['email'])  
        db.session.add(user)
        db.session.commit()
        return user

def update_user(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        db.session.commit()
        return user
    return None

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
