from flask import Blueprint, request, jsonify
from db.utils import fill_db
from db.models import *
from app.blueprints.dao.utils import User_db_worker as Users, Order_db_worker as Orders, Offer_db_worker as Offers

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.before_app_first_request
def init_db():
    fill_db('db/data/users.json', User)
    fill_db('db/data/orders.json', Order)
    fill_db('db/data/offers.json', Offer)

@main_blueprint.get('/')
def page_main():
    return jsonify({'status':'ok'})


# users
@main_blueprint.get('/users/')
def page_all_users():
    return jsonify(Users().get_all())
    # return db.session.query(Order, User).join((User, Order.customer_id == User.id)).all()

@main_blueprint.get('/users/<int:user_id>')
def page_user_by_id(user_id):
    return jsonify(Users().get_by_id(user_id))

@main_blueprint.post('/users/')
def add_new_user():
    # data should be send by Post application/json content type

    new_user_data = request.get_json()
    result = Users().add(new_user_data)
    return jsonify(result)

@main_blueprint.put('/users/<int:user_id>')
def update_user(user_id):
    new_user_data = request.get_json()
    result = Users().update(user_id, new_user_data)
    return jsonify(result)

@main_blueprint.delete('/users/<int:user_id>')
def delete_user(user_id):
    result = Users().delete(user_id)
    return jsonify(result)


# orders
@main_blueprint.get('/orders/')
def page_all_orders():
    return jsonify(Orders().get_all())

@main_blueprint.get('/orders/<int:order_id>')
def page_order_by_id(order_id):
    return jsonify(Orders().get_by_id(order_id))

@main_blueprint.post('/orders/')
def add_new_order():
    # data should be send by Post application/json content type

    new_order_data = request.get_json()
    result = Orders().add(new_order_data)
    return jsonify(result)

@main_blueprint.put('/orders/<int:order_id>')
def update_order(order_id):
    new_order_data = request.get_json()
    result = Orders().update(order_id, new_order_data)
    return jsonify(result)

@main_blueprint.delete('/orders/<int:order_id>')
def delete_order(order_id):
    result = Orders().delete(order_id)
    return jsonify(result)


# offers
@main_blueprint.get('/offers/')
def page_all_offers():
    return jsonify(Offers().get_all())

@main_blueprint.get('/offers/<int:offer_id>')
def page_offer_by_id(offer_id):
    return jsonify(Offers().get_by_id(offer_id))

@main_blueprint.post('/offers/')
def add_new_offer():
    # data should be send by Post application/json content type

    new_offer_data = request.get_json()
    result = Offers().add(new_offer_data)
    return jsonify(result)

@main_blueprint.put('/offers/<int:offer_id>')
def update_offer(offer_id):
    new_offer_data = request.get_json()
    result = Offers().update(offer_id, new_offer_data)
    return jsonify(result)

@main_blueprint.delete('/offers/<int:offer_id>')
def delete_offer(offer_id):
    result = Offers().delete(offer_id)
    return jsonify(result)

