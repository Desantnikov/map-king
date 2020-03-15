import json
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, jwt_required
from flask_restful import Resource, reqparse

from .helpers import get_token_response, get_unexpected_error_response, get_token_model

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserModelResource(Resource):
    def __init__(self):
        from db.models.user import UserModel  # TODO: Find another way
        super().__init__()
        self.model = UserModel


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
            return get_unexpected_error_response(e)


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


class UserLogoutAccess(Resource):
    def __init__(self):
        self.model = get_token_model(token_type='access')

    @jwt_required
    def post(self):
        try:
            jti = get_raw_jwt()['jti']
            token_to_revoke = self.model(jti=jti)

            if not token_to_revoke.is_revoked():
                token_to_revoke.revoke()
                response_object = {
                    'status': 'Success',
                    'message': 'Token added to revoked list'
                }
                return json.dumps(response_object), 200

            response_object = {
                'status': 'Fail',
                'message': "Can't revoke revoked token"
            }
            return json.dumps(response_object), 400
        except Exception as e:
            return get_unexpected_error_response(e)


class UserLogoutRefresh(Resource):
    def __init__(self):
        self.model = get_token_model(token_type='refresh')

    @jwt_refresh_token_required
    def post(self):
        try:
            jti = get_raw_jwt()['jti']
            token_to_revoke = self.model(jti=jti)

            if not token_to_revoke.is_revoked():
                token_to_revoke.revoke()
                response_object = {
                    'status': 'Success',
                    'message': 'Token added to revoked list'
                }
                return json.dumps(response_object), 200

            response_object = {
                'status': 'Fail',
                'message': "Can't revoke revoked token"
            }
            return json.dumps(response_object), 400
        except Exception as e:
            return get_unexpected_error_response(e)


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

# class DatabaseDebugResource(Resource):
#     def get(self):
#

