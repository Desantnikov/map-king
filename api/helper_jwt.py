import json

from app import jwt_manager


def get_token_response(user):
    access_token = user.get_access_token()
    refresh_token = user.get_refresh_token()

    response_object = {
        'status': 'Success',
        'message': 'Successfully authenticated.',
        'auth_token': access_token,
        'refresh_token': refresh_token
    }

    return json.dumps(response_object), 200


@jwt_manager.expired_token_loader
def get_token_expired_response(expired_token):
    token_type = expired_token['type']
    return json.dumps({
        'status': 401,
        'sub_status': 42,
        'msg': 'The {} token has expired'.format(token_type)
    }), 401
