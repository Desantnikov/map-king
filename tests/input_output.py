from tests.helpers import check_token, random_string


REGISTRATION_CHECK_INPUT = list()  # (type, {url, {data}, {headers}})
REGISTRATION_CHECK_INPUT.append(('post', {'url': '/registration',
                                          'data': {'username': random_string(),
                                                   'password': random_string()},
                                          'headers': None}))


REGISTRATION_CHECK_OUTPUT = list()
REGISTRATION_CHECK_OUTPUT.append({'status': 'Success',
                                  'message': 'Successfully authenticated.',
                                  'auth_token': check_token,
                                  'refresh_token': check_token})
