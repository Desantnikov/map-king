import cell
from map import Map
from player import Player
from liberty import Liberty
import time
import json


class Room:
    def __init__(self, id, players_amount, type, map_size):
        self.id = id
        self.owner_token = time.time()
        self.players_amount = players_amount
        self.type = type
        self.map_size = map_size

        self.players = []
        for new_player in range(players_amount):  # Player 0 == no one
            self.players.append(Player(new_player, map_size // players_amount))

        self.map = Map(map_size, self.players)


    def get_map(self):
        return json.dumps([self.map.serialize()], separators=(',', ': '), sort_keys=True, indent=4)
        # TODO: return self.serialize()

    def get_info(self):
        return json.dumps([self.id, self.type, self.map.serialize()])





