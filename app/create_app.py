from flask import Flask
from app.blueprints.views import main_blueprint
from db.db_init import db

app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False

db.init_app(app)