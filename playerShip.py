__author__ = 'David'


class PlayerShip:
    def __init__(self, windowx, windowy):
        self.x = windowx//2
        self.y = windowy//2
        self.health = 10
        self.color = (255, 0, 0)
        self.object_type = "player_ship"
        self.direction = "up"
        self.level = 0
        self.radius = self.level + 5
        self.damage = 2