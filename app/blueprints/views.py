from flask import Blueprint, request, url_for, redirect, jsonify
from db.utils import fill_db
from db.models import *
from app.blueprints.dao.utils import get_all_users_list, get_user_by_id


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

@main_blueprint.route('/users/<int:user_id>')
def page_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))