import sys

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

from api.resources import UserRegistration, UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, AllUsers, \
    SecretResource, IndexResource
from db.db_config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY
from helpers import get_env_variable


def api_init(app):
    api = Api(app)

    api.add_resource(UserRegistration, '/registration')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogoutAccess, '/logout/access')
    api.add_resource(UserLogoutRefresh, '/logout/refresh')
    api.add_resource(TokenRefresh, '/token/refresh')
    api.add_resource(AllUsers, '/users')
    api.add_resource(SecretResource, '/secret')
    api.add_resource(IndexResource, '/')

    return api


def db_init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['DATABASE_URL'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY

    db = SQLAlchemy(app)

    @app.before_first_request  # is needed?
    def create_tables():
        db.create_all()

    return db



logger.add(sys.stdout, colorize=True)

flask_app = Flask(__name__)
api = api_init(flask_app)
db = db_init(flask_app)

CORS(flask_app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(flask_app, cors_allowed_origins="*", log=logger, channel='')
