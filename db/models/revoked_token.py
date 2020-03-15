import json
from flask_jwt_extended import create_access_token, create_refresh_token

from app import db
from json_encoder import UniversalJsonEncoder


class TokenModel(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'UserID: {self.id}; Username: {self.username};'

    def save_to_db(self):
        #db.session.begin()
        db.session.add(self)
        db.session.commit()