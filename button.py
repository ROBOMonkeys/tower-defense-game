from pygame import image, mouse


class ImageButton():
    """
A button class that allows the use of an image as the clickable aspect

Vars:
 img_path = path to image
 loc      = location to display the button
 callback = function to call when the button is clicked, defaults to None
    """
    
    def __init__(self, img_path, loc, callback=None):
        self.img = image.load(img_path).convert_alpha()
        self.location = loc
        self.height = self.img.get_height()
        self.width = self.img.get_width()
        self.callback = callback
        
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
