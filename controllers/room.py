from controllers.map import MapController
import json



class RoomController:
    def __init__(self, room):
        self.room = room
        self.map_controller = MapController(self.room.map)

    def turn(self, player_id, *args):
        if not self.check_turn() == player_id:
            return False, 'Not your turn'

        player = self.get_player_by_id(player_id)

        for x, y in args:
            if self.map_controller.step(player, x, y):
                print("Event happened")

        self.move_to_end()

    def check_path(self, *args):  # check for jumps
        pass

    def check_turn(self):  # cookie better
        return self.room.players_queue[-1].id

    def get_room_id(self):
        return self.room.id

    def get_player_by_id(self, player_id):
        return self.room.players[player_id]

    def join(self):
        return True

    def get_map(self):
        return json.dumps(self.map_controller.get_map().serialize())
        # TODO: return self.serialize(), move jsonify to main

    def get_info(self):
        return json.dumps([self.id, self.type, self.map.serialize()])

    def move_to_end(self):
        player = self.room.players_queue.popleft()
        self.room.players_queue.append(player)


