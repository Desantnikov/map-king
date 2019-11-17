

class Cell:
    def __init__(self, owner=None, x=None, y=None):#, occupied_by=None):
        self.owner = owner
        #self.x = x
        #self.y = y

    #def get_position(self):
    #    return self.x, self.y

    def serialize(self):
        return [self.owner.id]

    # def update(self, new_owner=None):
    #     if new_owner:
    #         self.owner = new_owner


    #def __contains__(self, players_list):
    #    for player in players_list:
    #        return all([self.x == player.x, self.y == player.y])
    #    return True if

