import sys

from loguru import logger

from config import DEFAULT_HEALTH_LEVEL, DEFAULT_ATTACK_LEVEL
from map_object import MapObject



class Nobody(MapObject):
    def __init__(self, x, y, id=None):
        super().__init__(x, y)
        self.id = id

    def __repr__(self):
        return 'Nobody'

    def __bool__(self):
        return False


class Player(Nobody):
    def __init__(self, id, x, y):
        super().__init__(x, y, id)
        self.health, self.attack = DEFAULT_HEALTH_LEVEL, DEFAULT_ATTACK_LEVEL

    def __str__(self):
        return f'PLAYER{self.id}'#HP: {self.health}; Attack: {self.attack};'

    def __repr__(self):
        return f'PLAYER{self.id}'#HP: {self.health}; Attack: {self.attack};'

    def __bool__(self):
        return True

    def change_location(self, x, y):
        self.x, self.y = x, y
        return True

    def get_info(self):
        return {'id': self.id, 'health': self.health, 'attack': self.attack}

    def take_damage(self, damage):
        if self.health > damage:
            self.health -= damage
            return True
        return False  # player died

    def calculate_damage(self, type='regular'):
        if type == 'regular':
            return self.attack
        # else skills, items and other stuff that can change final damage




