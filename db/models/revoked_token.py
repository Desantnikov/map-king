from sqlalchemy.sql.expression import select, exists

from app import db
from json_encoder import UniversalJsonEncoder


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
        return db.session.query(exists().where(self.__class__.jti == self.jti))

    def revoke(self):
        db.session.add(self)
        db.session.commit()


class RevokedRefreshTokenModel(RevokedAccessTokenModel):
    __tablename__ = "revoked_refresh_tokens"
    token_type = 'refresh'
