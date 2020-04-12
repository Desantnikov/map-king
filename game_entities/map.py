from random import choice
from loguru import logger

from game_entities.player import Nobody  # import from module not from file
from .cell import Cell
from .config import VALID_POSITION_DELTAS, ENEMIES_AMOUNT_MULTIPLIER
from .events import Fight


class Map:
    def __init__(self, width, height, players):
        self.width = width
        self.height = height
        # creating 2-dim list with cells, assigning a position to each, occupying by new Nobody,
        # (one cell - one Nobody with new coords), choosing random cell type
        self.cells = [[Cell(x, y, choice(Cell.all_types)) for x in range(width)] for y in range(height)]
        self.players, self.enemies = players, []
        self.enemies_add()

    def step(self, player, position_delta):
        prev_x, prev_y = player.x, player.y
        delta_x, delta_y = position_delta
        new_x, new_y = prev_x + delta_x, prev_y + delta_y  # Separate method for calcs

        is_turn_valid, err = self._check_turn(prev_x, prev_y, new_x, new_y)
        if not is_turn_valid:
            return False, err

        if self.cells[new_x][new_y].occupied:
            target = self.players[self.cells[new_x][new_y].occupied_by]
            logger.info(f'Cell is already occupied by player {self.cells[new_x][new_y].occupied_by}, fighting;')
            fight = Fight(player, target)
            status, message = fight.regular_hit()
            if status != 0:  # player don't change position if target didn't die
                return status, message

        self.cells[prev_x][prev_y].occupy(Nobody(prev_x, prev_y))  # leave cell
        self.cells[new_x][new_y].occupy(player)  # occupy new cell
        player.change_location(new_x, new_y)  # update player's coords

        return True, f'Stepped successfully'

    def enemies_add(self):
        from game_entities.enemy import Enemy

        amount_to_add = int(self.width * self.height * ENEMIES_AMOUNT_MULTIPLIER)
        while len(self.enemies) < amount_to_add:
            self.enemies.append(Enemy(*self.get_random_not_occupied_cell().get_location()))

    def get_random_not_occupied_cell(self):
        cell = choice(choice(self.cells))
        if cell.occupied:
            return self.get_random_not_occupied_cell()
        return cell

    def _check_turn(self, prev_x, prev_y, new_x, new_y):
        if (prev_x - new_x, prev_y - new_y) not in VALID_POSITION_DELTAS:
            logger.error(f'Player {self.id} tried to jump from X,Y:{self.get_location()} to (X,Y):{(x,y)};'
                         f'Valid position deltas are: {VALID_POSITION_DELTAS}')
            return False, 'Invalid step distance'
        if prev_x + new_x < 0 or prev_y + new_y < 0:
            logger.error(f'Player {self.id} tried to jump from X,Y:{self.get_location()} to (X,Y):{(x,y)};'
                         f'Coordinates < 0 are not valid')
            return False, 'Out of borders'

        return True, ''

    def get_dict(self):
        return [[{'occupied_by': cell.occupied_by,
                  'foregroung_objects_list': cell.foregroung_objects_list,
                  'cell_type': cell.cell_type} for cell in line] for line in self.cells]
