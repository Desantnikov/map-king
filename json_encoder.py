from json import JSONEncoder

from cell import Cell
from player import Player, Nobody


class UniversalJsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, (Player, Nobody)):
                return o.id  # only id for player, image name stored in cell

            elif isinstance(o, Cell):
                return {'occupied_by': o.occupied_by, 'cell_type': o.cell_type,
                        'foregroung_objects_list': o.foregroung_objects_list}

            elif o.__class__.__name__ == 'UserModel':  # no import no circular dependency
                return {'username': o.username, 'password': o.password}

            elif o.__class__.__name__ in ['RevokedRefreshTokenModel', 'RevokedAccessTokenModel']:
                return {'type': o.get_type(), 'jti': o.jti}

        except:
            return JSONEncoder.default(self, o)



