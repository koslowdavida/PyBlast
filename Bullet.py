__author__ = 'David'


class Bullet:
    color = (255, 255, 255)
    damage = 2


    def __init__(self, x, y, direction, ship_radius, dam):
        self.x = x
        if direction == "up":
            self.y = y - 25
            self.speed = 15
        else:
            self.y = y + 25
            self.speed = 10

        self.direction = direction
        self.bump = False
        self.radius = int(ship_radius * .15)
        self.damage = dam
