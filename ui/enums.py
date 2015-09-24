from pygame import mouse, image
from os import path

RESOURCES = path.dirname(path.realpath(__file__)) + "/../test-res/"

DEFAULT_FONT = RESOURCES + "fonts/FiraSans-Light.ttf"
DEFAULT_SIZE = 24

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

MAPS = []
CUR_MAP = 0
PATHS = []

TILE_H = 32
TILE_W = 32

class Drawable():
    def isDrawable(self, obj_to_test):
        """
        Checks to see if an object has inherited from Drawable
        
        Vars:
         obj_to_test = object to test
        """
        return type(self) in obj_to_test.__class__.__bases__
    
    def draw(self, srf):
        """
        Draws the button onto the specified surface
        
        Vars:
         srf = Surface object to draw the object on
        """
        if type(self.srf) == list:
            for surface in self.srf:
                if not self.isDrawable(surface) and \
                   surface.__class__.__name__ != "Surface":
                    srf.blit(surface.srf, surface.location)
                elif self.isDrawable(surface):
                    surface.draw(srf)
                else:
                    srf.blit(surface, self.location)
        else:
            if self.location is not None:
                srf.blit(self.srf, self.location)


class Clickable(Drawable):
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


