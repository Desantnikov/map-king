from loguru import logger

from player import Nobody
from map_object import MapObject

class Cell(MapObject):
    def __init__(self, x, y, owner):
        super().__init__(x, y)
        self.owner = self.occupied_by = owner.id


    def __str__(self):
        return f'Owner: {self.owner}; Occupied by: {self.occupied_by}; Position: {self.get_location()}'

    def __repr__(self):
        return f'{self.get_pos()}'

    def is_occupied(self):
        return self.occupied_by is not None

    occupied = property(is_occupied)

    def occupy(self, player):
        if player:
            self.owner = player.id

        self.occupied_by = player.id

        return True




