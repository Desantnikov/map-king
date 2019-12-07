from player import Player, Nobody
from cell import Cell


from json import JSONEncoder


class UniversalJsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, (Player, Nobody)):
                #return f'Player {o.id}; {o.health} HP;'
                return o.id
            elif isinstance(o, Cell):
                #return f'(X,Y):{o.get_pos()}; Occupied by: {o.occupied_by}'
                return o.occupied_by
        except:
            return JSONEncoder.default(self, o)



