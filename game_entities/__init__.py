from .room import Room
from .player import Player
from .enemy import Enemy
from .skills import get_skills_list, SKILLS

from .config import MAP_SETTINGS, MAP_DEFAULTS

rooms = []


def create_new_room(request_data):
    settings = [request_data.get(*parameter) for parameter in zip(MAP_SETTINGS, MAP_DEFAULTS)]
    parameters = settings + [len(rooms)]  # width, height, players, room_id
    rooms.append(Room(*parameters))

    # from random import choice  # until map generation will be done
    # [choice(choice(rooms[-1].map.cells)).add_on_foreground('snake') for x in range(5)]
    # [choice(choice(rooms[-1].map.cells)).add_on_foreground('sign') for x in range(5)]

    return rooms[-1]


def get_all_rooms_list():
    return [str(room) for room in rooms] if rooms else None
