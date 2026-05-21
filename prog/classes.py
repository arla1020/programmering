import random 

class Character:
    def __init__(self, name, age, hp, damage):
        self.name = name
        self.age = age
        self.hp = hp
        self.damage = damage

    def random_damage(self):
        self.damage = random.choice([43, 44, 55, 64, 25, 87, 96, 100])



character1 = Character("Japan", 489, 6900, 43)

print(character1.damage)
character1.random_damage()
print(character1.damage)