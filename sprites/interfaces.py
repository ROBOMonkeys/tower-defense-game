class Moveable():
    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass


class Creature(Moveable):
    def __init__(self):
        self.damage = 0
        self.hp = 0
        self.speed = 0
