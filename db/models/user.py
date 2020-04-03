from flask_jwt_extended import create_access_token, create_refresh_token
from sqlalchemy import exists

from main import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'UserID: {self.id}; Username: {self.username};'

    def get_user_data(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}

    def save_to_db(self):
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
        return {'users': [user.get_user_data() for user in list(cls.query.all())]}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}


class RevokedAccessTokenModel(db.Model):
    __tablename__ = "revoked_access_tokens"
    token_type = 'access'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(256), nullable=False)  # Not sure that it can't bo longer

    # timestamp?

    def __repr__(self):
        return f'Token type {self.get_type()} was revoked: {self.id};'

    def get_type(self):
        return self.__class__.token_type

    def is_revoked(self):
        return db.session.query(exists().where(self.__class__.jti == self.jti)).scalar()

    def revoke(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        return {f'{cls.token_type} tokens': [{'type': token.get_type(), 'jti': token.jti} for token in
                                             list(cls.query.all())]}


class RevokedRefreshTokenModel(RevokedAccessTokenModel):
    __tablename__ = "revoked_refresh_tokens"
    token_type = 'refresh'
