from flask_restful import Api

from .resources.authorization import UserRegistration, UserLogin, UserLogoutAccess, UserLogoutRefresh, \
    TokenRefresh, AllUsers, SecretResource, DatabaseDebugResource, User
from .resources.game import Game


def api_init(app):
    api = Api(app)

    # JWT, debug
    # TODO: change urls to /api/...
    api.add_resource(UserRegistration, '/registration')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserLogoutAccess, '/logout/access')
    api.add_resource(UserLogoutRefresh, '/logout/refresh')
    api.add_resource(TokenRefresh, '/token/refresh')
    api.add_resource(User, '/user')
    api.add_resource(AllUsers, '/users')
    api.add_resource(SecretResource, '/secret')
    api.add_resource(DatabaseDebugResource, '/debug/show_db')

    # Game
    api.add_resource(Game, '/api/game')

    return api

