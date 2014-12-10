__author__ = 'David'
import random
colors = [(0, 255, 255), (0, 255, 0), (0, 0, 255), (255, 0, 255)]

class EnemyShip:
    object_type = "enemy_ship"
    direction = "down"
    radius = 33
    speed = 4
    def __init__(self):
        self.x = random.randrange(50, 750)
        self.y = -50
        self.position = [self.x, self.y]
        self.color = colors[random.randrange(4)]
        self.health = 5
        self.shoot_countdown = random.randrange(30, 80)
        self.direction = "down"


