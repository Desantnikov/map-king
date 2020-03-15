import json
from flask_jwt_extended import create_access_token

from app import db, jwt_manager
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
        db.session.add(self)
        db.session.commit()

    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            return create_access_token(identity=self.username)
        except Exception as e:
            return e
    #
    # def decode_auth_token(auth_token):
    #     """
    #     Decodes the auth token
    #     :param auth_token:
    #     :return: integer|string
    #     """
    #     try:
    #         payload = jwt.decode(auth_token, os.getenv('SECRET_KEY', SECONDARY_SECRET_KEY))  # TODO: Set env var
    #         return payload['sub']
    #     except jwt.ExpiredSignatureError:
    #         return 'Signature expired. Please log in again.'
    #     except jwt.InvalidTokenError:
    #         return 'Invalid token. Please log in again.'

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


