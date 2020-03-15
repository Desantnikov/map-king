import random
from string import ascii_letters


def random_string(length=10):
    return ''.join([random.choice(ascii_letters) for _ in range(length)])


def check_token(jwt_token):
    return len(jwt_token) > 30
