from flask import Blueprint, request, url_for, redirect, jsonify
from db.utils import fill_db
from db.models import *
from app.blueprints.dao.utils import get_all_users_list, get_user_by_id, get_all_orders_list, get_order_by_id, \
    get_all_offers_list, get_offer_by_id

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.before_app_first_request
def init_db():
    fill_db('db/data/users.json', User)
    fill_db('db/data/orders.json', Order)
    fill_db('db/data/offers.json', Offer)

@main_blueprint.route('/users/')
def page_all_users():
    return jsonify(get_all_users_list())
    # return db.session.query(Order, User).join((User, Order.customer_id == User.id)).all()

@main_blueprint.get('/users/<int:user_id>')
def page_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))

@main_blueprint.get('/orders/')
def page_all_orders():
    return jsonify(get_all_orders_list())

@main_blueprint.get('/orders/<int:order_id>')
def page_order_by_id(order_id):
    return jsonify(get_order_by_id(order_id))

@main_blueprint.get('/offers/')
def page_all_offers():
    return jsonify(get_all_offers_list())

@main_blueprint.get('/offers/<int:offer_id>')
def page_offer_by_id(offer_id):
    return jsonify(get_offer_by_id(offer_id))

@main_blueprint.post('/users/')
def add_new_user():
    ...
    # return jsonify(get_all_users_list())
