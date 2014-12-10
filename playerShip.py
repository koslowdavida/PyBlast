__author__ = 'David'


class PlayerShip:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.health = 10
        self.color = (255, 0, 0)
        self.object_type = "player_ship"
        self.direction = "up"