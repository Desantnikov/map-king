from helpers import PytestRegex as regex
from helpers import random_string

INPUT_OUTPUT_DICT = {}

# ----------------------------------
# Registration test
INPUT = [['post', {'url': '/registration',
                   'data': {'username': random_string(),
                            'password': random_string()},
                   'headers': None}]]

EXPECTED_OUTPUT = [{'status': 'Success',
                    'message': 'Successfully authenticated.',
                    'auth_token': regex('.*'),
                    'refresh_token': regex('.*')}]

INPUT_OUTPUT_DICT.update({'registration': [INPUT[:], EXPECTED_OUTPUT[:]]})
# ----------------------------------


# Login test
INPUT = [['post', {'url': '/login',
                   'data': {'username': 'test',
                            'password': 'test'},
                   'headers': None}]]

INPUT_OUTPUT_DICT.update({'login': [INPUT[:], EXPECTED_OUTPUT[:]]})
# ----------------------------------


# JWT access test
INPUT = [['get', {'url': '/', 'headers': None}]]
EXPECTED_OUTPUT = ['Please use /room/new test']

INPUT_OUTPUT_DICT.update({'jwt_access': [INPUT[:], EXPECTED_OUTPUT[:]]})
