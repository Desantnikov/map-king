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
            elif o.__class__.__name__ == 'UserModel': #
                return {'username': o.username, 'password': o.password}

        except:
            return JSONEncoder.default(self, o)



