__author__ = 'David'


class Bullet:
    color = (255, 255, 255)
    damage = 2
    radius = 5
    speed = 13

    def __init__(self, x, y, direction):
        self.x = x
        if direction == "up":
            self.y = y - 25
        else:
            self.y = y + 25

        self.direction = direction
        self.bump = False
