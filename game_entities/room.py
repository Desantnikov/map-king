from collections import deque

from loguru import logger

from .map import Map
from .player import Player

from .config import STEPS_PER_TURN, DIRECTIONS, ROOM_INFO


class Room:
    def __init__(self, map_width, map_height, players_amount, room_id):
        self.id = room_id
        self.players_amount = players_amount

        # TODO: iterate over list of real ids
        self.players = [Player(None, *self.calc_start_pos(id, map_width)) for id in range(self.players_amount)]
        self.map = Map(map_width, map_height, self.players)

        self.turn_owner_queue = None#deque(range(self.players_amount))
        self.steps_left = deque(range(STEPS_PER_TURN))
        self.initial_update()

    def __str__(self):
        return ROOM_INFO.format(self.id, len(self.players), self.turn_owner_queue[0], self.steps_left[0])

    def new_player_connected(self, user_id):
        print(f'New player {user_id} arrived')
        for player in self.players:
            if not player.id_:  # id None -> free slot
                player.id_ = user_id
                break

    def count_free_slots(self):
        return len(list(filter(lambda x: not bool(x.id_), self.players)))

    def turn(self, player_id, direction):
        if player_id != self.turn_owner_queue[0]:
            logger.error(f'It"s Player {self.turn_owner_queue[0]} turn; You are Player {player_id};')
            return False, self.turn_owner_queue[0]

        position_delta = DIRECTIONS[direction]
        status, message = self.map.step(self.find_player_by_database_id(player_id), position_delta, )

        logger.info(f'Step-response is: {status}; Info: {message};')

        self.update_turn() if status else logger.error(f'Failed to make a turn')

        return status, self.turn_owner_queue[0]

    def ready_to_start(self):
        if all([player.id_ for player in self.players]):
            self.turn_owner_queue = deque([player.id_ for player in self.players])
            self.initial_update()
            print('All players arrived, we may start')
            return True
        return False

    def find_player_by_database_id(self, db_id):
        for player in self.players:
            if player.id_ == db_id:
                return player

    def update_turn(self):
        self.steps_left.rotate(1)
        if not self.steps_left[0]:
            self.turn_owner_queue.rotate(-1)
        return self.turn_owner_queue[0]

    def calc_start_pos(self, id, map_width):
        return map_width // self.players_amount * id, 0  # TODO: Rework

    def initial_update(self):  # Make an in-place cells occupying when creating a new object&
        for object in self.players + self.map.enemies:
            x, y = object.get_location()
            self.map.cells[x][y].occupy(object)

