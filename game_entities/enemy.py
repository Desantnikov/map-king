from random import choice

from game_entities import Player
from game_entities.enemies_list import ENEMIES_DICT


class Enemy(Player):
    counter = 2000  # start numerating from 2000 to avoid intersection with player's ids

    def __init__(self, x, y, name=choice(list(ENEMIES_DICT.keys()))):
        super().__init__(Enemy.counter, x, y)

        self.health, self.attack = ENEMIES_DICT[name]['health'], ENEMIES_DICT[name]['health']
        Enemy.counter += 1
