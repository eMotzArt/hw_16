from db.db_init import db
from db.models import User, Offer, Order

def get_all_users_list():
    all_users = db.session.query(User).all()
    to_return = [one.to_dict() for one in all_users]
    return to_return

def get_user_by_id(id):
    user = db.session.query(User).get(id).to_dict()
    return user