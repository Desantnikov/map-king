import sys

from loguru import logger

from config import POSITION_DELTA
from map_object import MapObject

#logger.add(sys.stdout, format="{message} \r\n ------------------------", level="DEBUG") # ??


class Nobody(MapObject):
    def __init__(self, x, y, id=None):
        super().__init__(x, y)
        self.id = id
        ##logger.info(f'{self} is now standing on cell (X,Y): {self.get_location()}')

    def __repr__(self):
        return 'Nobody'

    def __bool__(self):
        return False


class Player(Nobody):
    def __init__(self, id, x, y):
        super().__init__(x, y, id)  # logger = logger ?
        #logger = logger
        #self.id = id_
        #self.x = x
        #self.y = y
        #logger.info(f'Player{self.id} created and placed on (X,Y): {self.get_location()}')

    def __str__(self):
        return f'PLAYER{self.id}'

    def __repr__(self):
        return f'PLAYER{self.id}'

    def __bool__(self):
        return True

    def change_location(self, x, y):
        if self._check_turn(x, y):
            #logger.info(f'Player {self.id} was standing on cell (X,Y):{self.get_location()}')
            self.x, self.y = x, y
            #logger.info(f'Player {self.id} now stands on cell (X,Y):{self.get_location()}')
            return True
        return False

    def _check_turn(self, x, y):
        if {x, y} not in POSITION_DELTA: # or x == y == 0 turn skip ok?
            logger.error(f'Player {self.id} tried to jump from X,Y:{self.get_location} to (X,Y):{(x,y)};'
                              f'Valid position deltas are: {POSITION_DELTA}')
            return False
        if self.x + x < 0 or self.y + y < 0:
            logger.error(f'Player {self.id} tried to jump from X,Y:{self.get_location} to (X,Y):{(x,y)};'
                             f'Coordinates < 0 are not valid')
            return False

        return True




