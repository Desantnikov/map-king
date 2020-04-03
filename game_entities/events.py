from .map_object import MapObject

class Event(MapObject):
    def __init__(self, x, y, id):
        super().__init__(x, y)
        self.id = id


class Fight:
    def __init__(self, attacker, target):
        self.attacker, self.target = attacker, target

    def regular_hit(self):
        damage = self.attacker.calculate_damage()
        target_survived = self.target.take_damage(damage)
        if not target_survived:
            return 0, f'{self.target} died after taking {self.attacker} damage from {self.attacker}'

        return 1, f'{self.attacker} dealed {damage} damage to {self.target}, now he has {self.target.health} hp left;'
