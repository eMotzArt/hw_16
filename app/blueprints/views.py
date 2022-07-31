from flask import Blueprint, request, url_for, redirect, jsonify
from db.utils import fill_db
from db.models import *


main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.before_app_first_request
def init_db():
    fill_db('db/data/users.json', User)
    fill_db('db/data/orders.json', Order)
    fill_db('db/data/offers.json', Offer)

@main_blueprint.route('/')
def main_page():
    return jsonify(db.session.query(Order).first().to_dict())
