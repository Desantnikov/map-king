


def get_token_response(user):
    access_token = user.get_access_token()
    refresh_token = user.get_refresh_token()

    response_object = {
        'status': 'Success',
        'message': 'Successfully authenticated.',
        'auth_token': access_token,
        'refresh_token': refresh_token
    }
    return response_object, 200


def get_unexpected_error_response(exception):
    response_object = {
        'status': 'fail',
        'message': f'Unexpected error happened: {exception}'
    }
    return response_object, 401


def get_token_model(token_type=None):  # not good?
    from db.models.user import RevokedAccessTokenModel, RevokedRefreshTokenModel
    model_map = {'refresh': RevokedRefreshTokenModel, 'access': RevokedAccessTokenModel}
    try:
        return model_map[token_type]
    except KeyError:
        raise Exception(f"{token_type} model requested, only: {' ; '.join(model_map.keys())} are present")


