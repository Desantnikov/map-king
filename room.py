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
        for new_player in range(players_amount):
            self.players.append(Player(new_player, map_size // players_amount))

        self.map = Map(map_size, self.players)

    def join(self):
        return True

    def get_map(self):
        return json.dumps(self.map.serialize())
        # TODO: return self.serialize(), move jsonify to main

    def get_info(self):
        return json.dumps([self.id, self.type, self.map.serialize()])





