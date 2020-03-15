import json
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from flask_restful import Resource, reqparse

from .helper_jwt import get_token_response

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)

#parser.add_argument('jti', help='Used for revoking tokens', required=False)


class UserModelResource(Resource):
    def __init__(self):
        from db.models.user import UserModel  # TODO: Find another way
        super().__init__()
        self.model = UserModel


class RevokedTokenModelResource(Resource):
    def __init__(self):
        from db.models.revoked_token import RevokedTokenModel
        super().__init__()
        self.model = RevokedTokenModel


class UserRegistration(UserModelResource):
    def post(self):
        data = parser.parse_args()
        if self.model.find_by_username(data['username']):
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return json.dumps(response_object), 202

        new_user = self.model(username=data['username'], password=data['password'])
        try:
            new_user.save_to_db()
            return get_token_response(new_user)

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return json.dumps(response_object), 401


class UserLogin(UserModelResource):
    def post(self):
        data = parser.parse_args()
        current_user = self.model.find_by_username(data['username'])
        if not current_user:
            return {'message': f'User {data["username"]} doesn\'t exist'}

        if data.get('password') == current_user.password:
            current_user.save_to_db()
            return get_token_response(current_user)

        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(RevokedTokenModelResource):
    def post(self):
        # new_revoked_token = self.model(username=data['jti'])
        # try:
        #     new_user.save_to_db()
        #     return get_token_response(new_user)
        # jti = get_raw_jwt()['jti']
        # self.model.add(jti)
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        return get_token_response(current_user)


class AllUsers(UserModelResource):
    def get(self):
        return self.model.return_all()


class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }

