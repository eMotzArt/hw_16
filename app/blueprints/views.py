from flask import Blueprint, request, url_for, redirect, jsonify

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def main_page():
    return 'OK'
