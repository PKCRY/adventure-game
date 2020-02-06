import weapons
import random

#Basic enemy class
class Enemy(object):
    
    pass


class Goblin(Enemy):
    
    def __init__(self):
        self.weapon = weapons.Sword()

class Ork(Enemy):
    pass
