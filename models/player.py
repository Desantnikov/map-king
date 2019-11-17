import time

class Player:  # TODO: inherit from liberty
    def __init__(self, id, offset):
        self.id = id
        self.location = {'x': offset * id,  # TODO: rework
                         'y': 0}
        self.token = time.time()

    def serialize(self):
        return {'id': self.id,
                'location': self.location}

    @property
    def x(self):
        return self.location['x']

    @property
    def y(self):
        return self.location['y']

