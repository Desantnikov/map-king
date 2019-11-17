import time

class PlayerController:  # TODO: inherit from liberty
    def __init__(self, player):
        self.player = player

    def set_pos(self, x, y):
        self.player.x, self.player.y = x, y

    def get_pos(self):
        return (self.player.x, self.player.y)

    def get_player(self):
        return self.player

