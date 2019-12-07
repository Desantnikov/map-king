from map import Map
from player import Player

from config import STEPS_PER_TURN, DIRECTIONS, ROOM_INFO


class Room:
    def __init__(self, map_width, map_height, players_amount, room_id, logger):
        self.id = room_id  # TODO: Hash?
        self.log = logger
        self.map = Map(map_width, map_height, logger)
        self.players_amount = players_amount
        self.players = [Player(local_id, *self.calc_start_pos(local_id)) for local_id in range(players_amount)]
        self.initial_update()  # Update map with initial players position

        self._turn_owner = 0
        self.steps_left = 3

        self.log.write(f'Room with {len(self.players)} players and ID:{self.id} created')

    def __str__(self):
        return ROOM_INFO.format(self.id, len(self.players), self.get_turn_owner(), self.steps_left)

    def turn(self, player_id, direction):
        self.log.write(f'Player {player_id} with ID{player_id} turns {direction}')
        if not DIRECTIONS.get(direction):  # Necessary?&
            err = f'Wrong direction: {direction}; Possible directions: {DIRECTIONS.keys()}'
            self.log.error(err)
            raise ValueError(err)

        self.log.write(f'Direction {direction} is valid; Turn owner {self.get_turn_owner()}; Your ID: {player_id}')
        if self.get_turn_owner() != player_id:
            err = f'You are player {player_id}; Player {self.get_turn_owner()} should turn now'
            self.log.error(err)
            return False, err

        player, position_delta = self.players[player_id], DIRECTIONS[direction]
        self.log.write(f'Checks passed, player {player} stepping {direction}')

        status, cell_content = self.map.step(player, position_delta)

        self.log.write(f'Player stands on cell' if status else f'Failed to stand on cell')

        return status, self.get_turn_owner(change=True)


    def get_turn_owner(self, change=False):  # Change when turning, don't change when comparing to player's id
        if change:                           # Maybe change every second (third ?) call
            if self.steps_left:              # Steps amount decreased if != 0
                self.steps_left -= 1

            if not self.steps_left:     # else?
                self.steps_left = STEPS_PER_TURN
                if self._turn_owner < len(self.players):  # If last player's step - new round, zero player's turn
                    self._turn_owner += 1
                else:
                    self._turn_owner = 0
        return self._turn_owner

    def calc_start_pos(self, id):
        # Place players
        return self.map.width // self.players_amount * id, self.map.height // self.players_amount * id


    def initial_update(self):
        self.log.write(f'Initial players positioning')
        for player in self.players:
            x, y = player.x, player.y

            self.log.write(f'Player {player} with ID{player.id} now stands on (X:Y): ({x}:{y})')
            self.map.cells[x][y] = str(player)

    def get_map(self):
        return self.map.get()

