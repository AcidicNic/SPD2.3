# By Kamran Bigdely
# Extract superclass

class Enemy:

    def __init__(self):
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage

class AngryMushroom(Enemy):

    def spread_poison(self):
        print('spreading poison!')


class AngryBot(Enemy):

    def __init__(self):
        super().__init__()
        self.n_bullets = 40

    def punch_iron_fist(self):
        print("punching with iron fist!")

    def shoot(self):
        print("shot a bullet!")
        self.n_bullets -= 1



class AgressiveAlligator(Enemy):

    def bite(self):
        print('bitting!')


AngryBot = AngryBot()
print("initial health level:", AngryBot.health)
AngryBot.take_damage(25)
print("took damage!")
print("current health level:",AngryBot.health)
