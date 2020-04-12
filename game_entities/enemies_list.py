from game_entities import get_skills_list

SNAKE = {'name': 'Snake',
         'health': 5,
         'Skills': get_skills_list('regular_attack')}

CREEPY_GHOST = {'name': 'Creepy Ghost',
                'health': 5,
                'skills': get_skills_list(('melee_attack', 'range_attack'))}

STALKER_GHOST = {'name': 'Stalker Ghost',
                 'health': 5,
                 'skills': get_skills_list(('melee_attack', 'range_attack'))}


ENEMIES_DICT = ({
    'Snake': SNAKE,
    'Creepy Ghost': CREEPY_GHOST,
    'Stalker Ghost': STALKER_GHOST
})
