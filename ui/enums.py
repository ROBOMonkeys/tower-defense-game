from pygame import mouse
from os import path

RESOURCES = path.dirname(path.realpath(__file__)) + "/../test-res/"

DEFAULT_FONT = RESOURCES + "fonts/FiraSans-Light.ttf"
DEFAULT_SIZE = 24


class Clickable():
    """
    Just an interface for clickable classes to inherit from
    """

    def isOver(self):
        """
        Returns True or False if the mouse is over the button when the
        MOUSEBUTTONDOWN event happened
        """
        ms_x, ms_y = mouse.get_pos()
        loc_x, loc_y = self.location
        
        if (ms_x < (loc_x + self.width) and
            ms_y > loc_y and
            ms_x > loc_x and
            ms_y < (loc_y + self.height)):
            return True
        else:
            return False
        
    def click(self):
        """
        Checks to see if the button was clicked, then runs the callback
        function if there was one
        """
        if self.isOver():
            if self.callback is not None:
                self.callback()

    def draw(self, srf):
        """
        Draws the button onto the specified surface
        
        Vars:
         srf = Surface object to draw the button on
        """
        srf.blit(self.img, self.location)
