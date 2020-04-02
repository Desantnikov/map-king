from loguru import logger

from player import Nobody
from map_object import MapObject


class Cell(MapObject):
    all_types = ('grass',)

    def __init__(self, x, y, owner, cell_type, foregroung_imgs_list=None):
        super().__init__(x, y)
        self.owner = self.occupied_by = owner.id
        self._cell_type = cell_type
        self._foregroung_objects_list = foregroung_imgs_list

    foregroung_objects_list = property()

    def __str__(self):
        return f'Owner: {self.owner}; Occupied by: {self.occupied_by}; Position: {self.get_location()}'

    def __repr__(self):
        return f'{self.get_pos()}'

    def cell_type(self):
        return self._cell_type

    @foregroung_objects_list.getter
    def foregroung_objects_list_getter(self):
        return self._foregroung_objects_list

    @foregroung_objects_list.setter
    def foregroung_objects_list_setter(self, foregroung_objects_list):
        self._foregroung_objects_list = foregroung_objects_list

    def pop_from_foreground(self):  # remove closest to point of view object
        return self._foregroung_objects_list.pop()

    def add_on_foreground(self, object_to_add):  # add new object on top of already existing objs
        if object_to_add:
            self._foregroung_objects_list.append(object_to_add.get_image_name())

    def is_occupied(self):
        return self.occupied_by is not None

    occupied, cell_type = property(is_occupied), property(cell_type)

    def occupy(self, player):  # no need to deoccupy bcs deoccupying == occupying by another player
        if player:
            self.owner = player.id
        else:
            # if occupiing by nobody (deoccupiing)
            # remove closest image from foreground (should be image of player that was standing here before)
            self.pop_from_foreground()

        self.occupied_by = player.id
        self.add_on_foreground(player.get_image_name())

        logger.info(f'Cell X,Y:{self.get_location()} is now occupied by {self.occupied_by};')


        return True




