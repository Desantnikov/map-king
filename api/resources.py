# from db.models.user_model import UserModel
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class userModelResource(Resource):
    def __init__(self):
        from db.models.user_model import UserModel  # looks not very good
        super().__init__()
        self.model = UserModel


class UserRegistration(userModelResource):
    def post(self):
        data = parser.parse_args()

        if self.model.find_by_username(data['username']):
            return {'message': f'User {data["username"]} already exists'}

        new_user = self.model(username=data['username'], password=data['password'])
        try:
            new_user.save_to_db()
            return {'message': f'User {data["username"]} was created'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(userModelResource):
    def post(self):
        data = parser.parse_args()
        current_user = self.model.find_by_username(data['username'])
        if not current_user:
            return {'message': f'User {data["username"]} doesn\'t exist'}

        if data['password'] == current_user.password:
            return {'message': f'Logged in as {current_user.username}'}
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers(userModelResource):
    def get(self):
        return self.model.return_all()

    def delete(self):
        return self.model.delete_all()


class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }


class IndexResource(Resource):
    def get(self):
        return 'Please use /rooms/new'
