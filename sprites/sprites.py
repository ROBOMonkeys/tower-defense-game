from interface import Creature, Intelligent


class AutoCreature(Creature, Intelligent):
    def __init__(self, frames):
        Creature.__init__(self, frames)



