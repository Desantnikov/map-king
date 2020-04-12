SKILLS = ({
    'melee_attack': {'damage': 1, 'range': 1}, # damage - multiplier
    'ranged_attack': {'damage': 1, 'range': 3} # final damage to provide = player's (npc) overall attack * damage

})


def get_skills_list(skills):
    skills = [SKILLS.get(name) for name in skills]
    if not all(skills):
        raise IndexError(f'Skill(s) not found: {list(filter(bool, skills))} ')
    return skills