import json
from flask_jwt_extended import create_access_token, create_refresh_token
from sqlalchemy import exists

from app import db

from json_encoder import UniversalJsonEncoder

from config import SECONDARY_SECRET_KEY


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'UserID: {self.id}; Username: {self.username};'

    def save_to_db(self):
        #db.session.begin()
        db.session.add(self)
        db.session.commit()

    def get_access_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            return create_access_token(identity=self.username)
        except Exception as e:
            return e

    def get_refresh_token(self):
        """
        Generates the Refresh Token
        :return: string
        """
        try:
            return create_refresh_token(identity=self.username)
        except Exception as e:
            return e

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        return {'users': [json.dumps(user, cls=UniversalJsonEncoder) for user in list(cls.query.all())]}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

