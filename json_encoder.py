from player import Player, Nobody
from cell import Cell

from json import JSONEncoder


class UniversalJsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, (Player, Nobody)):
                return o.id
            elif isinstance(o, Cell):
                return o.occupied_by
            elif o.__class__.__name__ == 'UserModel':  # no import no circular dependency
                return {'username': o.username, 'password': o.password}
            elif o.__class__.__name__ in ['RevokedRefreshTokenModel', 'RevokedAccessTokenModel']:
                return {'type': o.get_type(), 'jti': o.jti}

        except:
            return JSONEncoder.default(self, o)



