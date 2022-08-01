from flask import Blueprint, request, url_for, redirect, jsonify
from db.utils import fill_db
from db.models import *
from app.blueprints.dao.utils import get_all_users_list, get_user_by_id, \
                                     get_all_orders_list, get_order_by_id, \
                                     get_all_offers_list, get_offer_by_id, \
                                     add_new_user_to_db, update_user_info, delete_user_from_db, \
                                     add_new_order_to_db, update_order_info, delete_order_from_db, \
                                     add_new_offer_to_db, delete_offer_from_db, update_offer_info

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
    return jsonify(get_all_users_list())
    # return db.session.query(Order, User).join((User, Order.customer_id == User.id)).all()

@main_blueprint.get('/users/<int:user_id>')
def page_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))

@main_blueprint.post('/users/')
def add_new_user():
    # data should be send by Post application/json content type

    new_user_data = request.get_json()
    result = add_new_user_to_db(new_user_data)
    return jsonify({'status': result})

@main_blueprint.put('/users/<int:user_id>')
def update_user(user_id):
    new_user_data = request.get_json()
    result = update_user_info(user_id, new_user_data)
    return jsonify({'status': result})

@main_blueprint.delete('/users/<int:user_id>')
def delete_user(user_id):
    result = delete_user_from_db(user_id)
    return jsonify({'status': result})


# orders
@main_blueprint.get('/orders/')
def page_all_orders():
    return jsonify(get_all_orders_list())

@main_blueprint.get('/orders/<int:order_id>')
def page_order_by_id(order_id):
    return jsonify(get_order_by_id(order_id))

@main_blueprint.post('/orders/')
def add_new_order():
    # data should be send by Post application/json content type

    new_order_data = request.get_json()
    result = add_new_order_to_db(new_order_data)
    return jsonify({'status': result})

@main_blueprint.put('/orders/<int:order_id>')
def update_order(order_id):
    new_order_data = request.get_json()
    result = update_order_info(order_id, new_order_data)
    return jsonify({'status': result})

@main_blueprint.delete('/orders/<int:order_id>')
def delete_order(order_id):
    result = delete_order_from_db(order_id)
    return jsonify({'status': result})


# offers
@main_blueprint.get('/offers/')
def page_all_offers():
    return jsonify(get_all_offers_list())

@main_blueprint.get('/offers/<int:offer_id>')
def page_offer_by_id(offer_id):
    return jsonify(get_offer_by_id(offer_id))

@main_blueprint.post('/offers/')
def add_new_offer():
    # data should be send by Post application/json content type

    new_offer_data = request.get_json()
    result = add_new_offer_to_db(new_offer_data)
    return jsonify({'status': result})

@main_blueprint.put('/offers/<int:offer_id>')
def update_offer(offer_id):
    new_offer_data = request.get_json()
    result = update_offer_info(offer_id, new_offer_data)
    return jsonify({'status': result})

@main_blueprint.delete('/offers/<int:offer_id>')
def delete_offer(offer_id):
    result = delete_offer_from_db(offer_id)
    return jsonify({'status': result})

