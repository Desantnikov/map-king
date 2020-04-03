from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from .db_config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY


def db_init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['DATABASE_URL'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY

    db = SQLAlchemy(app)
    migrate = Migrate()

    return db


def jwt_init(app):
    jwt_manager = JWTManager(app)

    @jwt_manager.invalid_token_loader  # merge two functions into one?
    def get_invalid_token_response(invalid_token):
        token_type = invalid_token['type']
        return {
            'status': 401,
            'sub_status': 42,
            'msg': 'The {} token has expired'.format(token_type)
        }, 401

    @jwt_manager.expired_token_loader
    def get_token_expired_response(expired_token):
        token_type = expired_token['type']
        return {
            'status': 401,
            'sub_status': 42,
            'msg': 'The {} token has expired'.format(token_type)
        }, 401

    return jwt_manager



