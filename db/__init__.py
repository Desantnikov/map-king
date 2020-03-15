from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import flask_app
from db import SQLALCHEMY_DATABASE_URI
from db.db_config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY


def db_init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['DATABASE_URL'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY

    db = SQLAlchemy(app)
    migrate = Migrate()

    return db


db = db_init(flask_app)