import json


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



