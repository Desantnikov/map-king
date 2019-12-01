from .cell import Cell
from itertools import product
from liberty import Liberty


class Map:
    def __init__(self, size, players):
        self.size = size
        self.players = players
        self.indexes = list(product(list(range(self.size)), list(range(self.size))))

        self.liberty = Liberty()

        self.cells_list = [[Cell(owner=self.liberty) for x in range(self.size)] for y in range(self.size)]
        #self.update_occupied_cells()
        self.update_occupied_cells()

    def update_occupied_cells(self, players=None):
        if not players:
            players = self.players
        for player in players:
            print(f'Updating cell [{player.x}][{player.y}] with player {player.id}')
            self.cells_list[player.x][player.y].update(occupied_by=player)


    def serialize(self):
        cells = [[self.cells_list[x][y].serialize() for x in range(self.size)] for y in range(self.size)]
        return {'size': self.size,
                'players': [player.serialize() for player in self.players],
                'cells': cells}
