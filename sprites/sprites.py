from interface import Robot, Intelligent


class AutoRobot(Robot, Intelligent):
    def __init__(self, frames):
        Robot.__init__(self, frames)



