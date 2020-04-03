from loguru import logger

from player import Nobody
from map_object import MapObject


class Cell(MapObject):
    all_types = ('grass', 'road', 'field')

    def __init__(self, x, y, cell_type=None):
        super().__init__(x, y)
        self.owner = self.occupied_by = None
        self.cell_type = cell_type
        self.foregroung_objects_list = []

    occupied = property(lambda self: bool(self.occupied_by))

    def __str__(self):
        return f'Owner: {self.owner}; Occupied by: {self.occupied_by}; Position: {self.get_location()}'

    def __repr__(self):
        return f'{self.get_location()}'

    def pop_from_foreground(self):  # remove closest to point of view object
        return self.foregroung_objects_list.pop() if self.foregroung_objects_list else None # !!!

    def add_on_foreground(self, object_to_add):  # add new object on top of already existing objs
        if object_to_add:
            self.foregroung_objects_list.append(object_to_add.get_image_name())

    def occupy(self, player):  # no need to deoccupy bcs deoccupying == occupying by Nobody
        if player:
            self.owner = player.id_
        else:
            # if occupiing by nobody (deoccupiing)
            # remove closest image from foreground (should be image of player that was standing here before)
            self.pop_from_foreground()

        self.occupied_by = player.id_
        self.add_on_foreground(player.get_object_name())

        logger.info(f'Cell X,Y:{self.get_location()} is now occupied by {self.occupied_by};')

        return True




