from json import JSONEncoder

class Nobody:
    def __init__(self):
        self.id = None

    def __repr__(self):  # Looks not very good?
        return '-'


class Player(Nobody, JSONEncoder):
    def __init__(self, id, x, y):
        #JSONEncoder.default = Player.default
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self):
        return {'id': self.id, 'x': self.x, 'y': self.y}

    def __str__(self):
        return f'PLAYER{self.id}'


    def get_location(self):
        return self.x, self.y

    #@staticmethod
    def default(self, player):
        return {'id': player.id, 'x': player.x, 'y': player.y}
