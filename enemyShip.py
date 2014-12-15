__author__ = 'David'
import random
colors = [(0, 255, 255), (0, 255, 0), (0, 0, 255), (255, 0, 255)]

class EnemyShip():
    object_type = "enemy_ship"
    direction = "down"
    bump = False
    speed = 2
    def __init__(self, windowx):
        self.x = random.randrange(50, windowx-50)
        self.y = -50
        self.position = [self.x, self.y]
        self.color = colors[random.randrange(4)]
        self.radius = random.randrange(20, 40)
        self.health = self.radius
        self.shoot_countdown = random.randrange(30, 80)
        self.shoot_countdown_static = self.shoot_countdown
        self.direction = "down"

        self.damage = self.shoot_countdown//10


