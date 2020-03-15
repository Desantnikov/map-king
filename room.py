from collections import deque

from loguru import logger

from map import Map
from player import Player

from config import STEPS_PER_TURN, DIRECTIONS, ROOM_INFO


class Room:
    def __init__(self, map_width, map_height, players_amount, room_id):
        self.id = room_id  # TODO: Hash?
        self.players_amount = players_amount
        self.players = [Player(id, *self.calc_start_pos(id, map_width)) for id in range(self.players_amount)]
        self.map = Map(map_width, map_height, self.players)


        self.turn_owner_queue = deque(range(self.players_amount))
        self.steps_left = deque(range(STEPS_PER_TURN))
        self.initial_update()

    def __str__(self):
        return ROOM_INFO.format(self.id, len(self.players), self.turn_owner_queue[0], self.steps_left[0])

    def turn(self, player_id, direction):
        if player_id != self.turn_owner_queue[0]:
            logger.error(f'It"s Player {self.turn_owner_queue[0]} turn; You are Player {player_id};')
            return False, self.turn_owner_queue[0]

        position_delta = DIRECTIONS[direction]
        status, message = self.map.step(self.players[player_id], position_delta, )

        logger.info(f'Step-response is: {status}; Info: {message};')

        self.update_turn() if status else logger.error(f'Failed to make a turn')

        return status, self.turn_owner_queue[0]

    def update_turn(self):
        self.steps_left.rotate(1)
        if not self.steps_left[0]:
            self.turn_owner_queue.rotate(-1)
        return self.turn_owner_queue[0]

    def calc_start_pos(self, id, map_width):
        return map_width // self.players_amount * id, 0  # TODO: Rework

    def initial_update(self):
        for player in self.players:
            x, y = player.get_location()
            self.map.cells[x][y].occupy(player)

    def get_map(self):
        return self.map.get()

