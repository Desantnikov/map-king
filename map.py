from player import Player

class Map:
    def __init__(self, width, height, log):
        self.width = width
        self.height = height
        self.cells = [[[None] for _ in range(width)] for _ in range(height)]
        self.log = log

    def step(self, player, position_delta):
        self.log.write(f'Player {player} with ID{player.id} steps {position_delta} ')

        x, y = player.x, player.y
        delta_x, delta_y = position_delta
        new_x, new_y = x + delta_x, y + delta_y

        self.log.write(f'Currently player stands on position {x}:{y}; New position should be {new_x}:{new_y}')

        is_occupied, occupied_by = self.check_cell(self.cells[new_x][new_y], Player)
        if is_occupied:
            err = f'Cell is already occupied by player {occupied_by}'
            self.log.error(err)
            return False, occupied_by
        self.log.write(f'Cell is not occupied, OK to occupy')

        self.cells[x][y] = None
        self.log.write(f'Previous cell {x}:{y} cleared and now {self.cells[x][y]}')

        self.cells[new_x][new_y].append(player)
        self.log.write(f'Current cell {x}:{y} occupied and now {self.cells[x][y]}')

        return True, self.cells[new_x][new_y]

    def get(self):
        return self.cells

    @staticmethod
    def check_cell(cell, check_for=Player):
        if not isinstance(cell, list):
            err = f'Cell should contain list'
            raise ValueError(err)

        occupied = [content for content in cell if isinstance(content, check_for)]

        # Occupied or not
        # Occupied by
        return bool(occupied), occupied

    @staticmethod
    def serializer(obj):
        # Get Player location if cell occupied
        players_locations = [Map.check_cell(cell)[1].get_location() for cell in obj.cells if obj.check_cell(cell)[0]]

        serializable_cells = obj.cells
        for x, y in players_locations:
            obj.log.write(f'{x},{y} changed')
            serializable_cells[x][y] = str(obj.cells[x][y])

        return serializable_cells

