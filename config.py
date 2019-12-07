STEPS_PER_TURN = 5

DIRECTIONS = {'UP': (0, 1), 'DOWN': (0, -1), 'LEFT': (-1, 0), 'RIGHT': (1, 0), 'SKIP': (0, 0)}  # position delta

ROOM_INFO = """ 
                Room ID: {}; Players amount: {}; 
                Turn of player: {}; He has {} steps left
            """

MAP_SETTINGS = ('width', 'height', 'players')
MAP_DEFAULTS = (10, 10, 4) # Default values

MAP_AUTOCONFIGS = ('room_id', 'logger')  #

MAP_PARAMETERS = MAP_SETTINGS + MAP_AUTOCONFIGS
