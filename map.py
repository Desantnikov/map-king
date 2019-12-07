from loguru import logger

from player import Nobody
from cell import Cell


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y, Nobody(x, y)) for x in range(width)] for y in range(height)]

    def step(self, player, position_delta):


        prev_x, prev_y = player.x, player.y
        delta_x, delta_y = position_delta
        new_x, new_y = prev_x + delta_x, prev_y + delta_y  # Separate method for calcs



        if self.cells[new_x][new_y].occupied:  # convert to bool?
            err = f'Cell is already occupied by player {self.cells[new_x][new_y].occupied_by}'
            logger.error(err)

            # Return battle PvP event later
            return False, self.cells[new_x][new_y].occupied_by

        logger.info(f'Previous location: {prev_x, prev_y}; \r\n'
                    f'New location: {new_x, new_y}; \r\n ---------')

        self.cells[prev_x][prev_y].occupy(Nobody(prev_x, prev_y))  # leave cell
        self.cells[new_x][new_y].occupy(player)  # stand on new cell
        player.x, player.y = new_x, new_y

        return True, self.cells[new_x][new_y]

    def get(self):
        return self.cells




