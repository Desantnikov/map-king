from .skills import get_skills_list

SNAKE = {'name': 'Snake',
         'health': 5,
         'Skills': get_skills_list(('melee_attack', ))}

CREEPY_GHOST = {'name': 'Creepy Ghost',
                'health': 5,
                'skills': get_skills_list(('melee_attack', 'ranged_attack'))}

STALKER_GHOST = {'name': 'Stalker Ghost',
                 'health': 5,
                 'skills': get_skills_list(('melee_attack', 'ranged_attack'))}


ENEMIES_DICT = ({
    'Snake': SNAKE,
    'Creepy Ghost': CREEPY_GHOST,
    'Stalker Ghost': STALKER_GHOST
})
