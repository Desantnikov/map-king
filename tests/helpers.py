import random
import re
from string import ascii_letters


def random_string(length=10):
    return ''.join([random.choice(ascii_letters) for _ in range(length)])


def check_token(jwt_token):
    return len(jwt_token) > 30


class PytestRegex:
    """
    Custom class to make it possible for assertEqual to work with regexp
    """

    def __init__(self, pattern, flags=0):
        self._regex = re.compile(pattern, flags)

    def __eq__(self, actual):
        return bool(self._regex.match(actual))

    def __repr__(self):
        return self._regex.pattern
