STEPS_PER_TURN = 1

DIRECTIONS = {'LEFT': (-1, 0), 'RIGHT': (1, 0), 'DOWN': (0, 1), 'UP': (0, -1), 'SKIP': (0, 0)}  # position delta
# TODO: Make normal positioning (X,Y)

ROOM_INFO = """ 
                Room ID: {}; Players amount: {}; 
                Turn of player: {}; He has {} steps left
            """

MAP_SETTINGS = ('width', 'height', 'players')
MAP_DEFAULTS = (10, 10, 2)  # Default values

MAP_AUTOCONFIGS = ('room_id', 'logger')  #

MAP_PARAMETERS = MAP_SETTINGS + MAP_AUTOCONFIGS

POSITION_DELTA = [-1, 0, 1]  # to check for jumps