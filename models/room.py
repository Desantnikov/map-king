
from models.map import Map
from models.player import Player
from liberty import Liberty
import time
import json
from collections import deque


class Room:
    def __init__(self, id, players_amount, type, map_size):
        self.id = id
        self.owner_token = time.time()
        self.players_amount = players_amount
        self.type = type
        self.map_size = map_size


        self.players = (Player(new_player, map_size // players_amount) for new_player in range(players_amount))

        self.players_queue = deque(self.players)

        self.map = Map(map_size, self.players)




    def join(self):
        return True

    def get_map(self):
        return json.dumps(self.map.serialize())
        # TODO: return self.serialize(), move jsonify to main

    def get_info(self):
        return json.dumps([self.id, self.type, self.map.serialize()])





