from .player import PlayerController


class MapController:
    def __init__(self, map):
        self.map = map
        self.player_controllers = (PlayerController(player) for player in self.map.players)


    def step(self, player_id, x, y):
        self.player_controllers[player_id].turn(x, y)       # update player position
        self.map.cell_list[x][y].owner = self.player_controllers[player_id].get_player()   # own cell
        # if mob/player/other event on cell the return cell

        return None

    def get_map(self):
        return self.map