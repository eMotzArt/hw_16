from db.db_init import db
from db.models import User, Offer, Order

def get_all_users_list():
    all_users = db.session.query(User).all()
    to_return = [user.to_dict() for user in all_users]
    return to_return

def get_user_by_id(id):
    user = db.session.query(User).get(id).to_dict()
    return user

def get_all_orders_list():
    all_orders = db.session.query(Order).all()
    to_return = [order.to_dict() for order in all_orders]
    return to_return

def get_order_by_id(id):
    order = db.session.query(Order).get(id).to_dict()
    return order

def get_all_offers_list():
    all_offers = db.session.query(Offer).all()
    to_return = [offer.to_dict() for offer in all_offers]
    return to_return

def get_offer_by_id(id):
    offer = db.session.query(Offer).get(id).to_dict()
    return offer