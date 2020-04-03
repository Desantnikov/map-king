import sys
import os
import json

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager

from loguru import logger

from db import db_init
from api.resources import UserRegistration, UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, AllUsers, \
    SecretResource, DatabaseDebugResource, User




def api_init(app):
    api = Api(app)

    api.add_resource(UserRegistration, '/registration')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogoutAccess, '/logout/access')
    api.add_resource(UserLogoutRefresh, '/logout/refresh')
    api.add_resource(TokenRefresh, '/token/refresh')
    api.add_resource(User, '/user')
    api.add_resource(AllUsers, '/users')
    api.add_resource(SecretResource, '/secret')
    api.add_resource(DatabaseDebugResource, '/debug/show_db')
    return api


def jwt_init(app):
    jwt_manager = JWTManager(app)

    @jwt_manager.invalid_token_loader  # merge two functions into one?
    def get_invalid_token_response(invalid_token):
        token_type = invalid_token['type']
        return json.dumps({
            'status': 401,
            'sub_status': 42,
            'msg': 'The {} token has expired'.format(token_type)
        }), 401

    @jwt_manager.expired_token_loader
    def get_token_expired_response(expired_token):
        token_type = expired_token['type']
        return json.dumps({
            'status': 401,
            'sub_status': 42,
            'msg': 'The {} token has expired'.format(token_type)
        }), 401

    return jwt_manager


logger.add(sys.stdout, colorize=True)

flask_app = Flask(__name__)
jwt = jwt_init(flask_app)
api = api_init(flask_app)
db = db_init(flask_app)

flask_app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY', 'add_env_var')

CORS(flask_app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(flask_app, cors_allowed_origins="*", log=logger, channel='')
