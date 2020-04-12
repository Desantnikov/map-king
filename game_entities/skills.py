SKILLS = ({
    'melee_attack': {'damage': 1, 'range': 1}, # damage - multiplier
    'ranged_attack': {'damage': 1, 'range': 3} # final damage to provide = player's (npc) overall attack * damage

})


def get_skills_list(skills_list):
    skills = [SKILLS.get(name) for name in skills_list]
    if not all(skills):
        raise IndexError(f'Skills to found: {skills_list}; Found skills: {skills}')
    return skills