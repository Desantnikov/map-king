STEPS_PER_TURN = 1

DIRECTIONS = {'LEFT': (-1, 0), 'RIGHT': (1, 0), 'DOWN': (0, 1), 'UP': (0, -1), 'SKIP': (0, 0)}  # position delta


ROOM_INFO = """ 
                Room ID: {}; Players amount: {}; 
                Turn of player: {}; He has {} steps left
            """

MAP_SETTINGS = ('width', 'height', 'players')  # TODO: Get from user
MAP_DEFAULTS = (10, 10, 2)  # Default values

MAP_AUTOCONFIGS = ('room_id',)

MAP_PARAMETERS = MAP_SETTINGS + MAP_AUTOCONFIGS

VALID_POSITION_DELTAS = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]  # to check for jumps
DEFAULT_HEALTH_LEVEL = 10
DEFAULT_ATTACK_LEVEL = 1

RESPONSE_CODES = {0: 'Targed died;', 1: 'Target survived fight;'}



