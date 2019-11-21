

class Cell:
    def __init__(self, owner=None, x=None, y=None):#, occupied_by=None):
        self.owner = owner
        #self.x = x
        #self.y = y

    #def get_position(self):
    #    return self.x, self.y

    def serialize(self):
        return [self.owner.id]

    def update(self, occupied_by=None):
        if occupied_by:
            self.owner = occupied_by
            self.occupied_by = occupied_by
        else:
            self.occupied_by = None


    #def __contains__(self, players_list):
    #    for player in players_list:
    #        return all([self.x == player.x, self.y == player.y])
    #    return True if

