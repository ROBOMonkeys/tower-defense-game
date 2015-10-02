from pygame import mouse, font, image, transform
import util.enums
from util.util import ui_cover_up
import enums as ui_enums


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
                
    def update(self):
        if mouse.get_pressed()[0]:
            self.click()
        self.draw(util.enums.SCREEN)


class UIElement(Drawable):
    def __init__(self, img_path, location):
        self.srf = image.load(img_path).convert_alpha()
        self.location = location

    def update_element(self, img_path, btm):
        dims = (self.srf.get_height(), self.srf.get_width())
        ui_cover_up(self.location, dims, btm)
        self.srf = image.load(img_path).convert_alpha()
        self.draw(util.enums.SCREEN)


class UIString(Drawable):
    def __init__(self, text, location, color=(0, 0, 0)):
        if not font.get_init():
            font.init()
        self.fnt = font.Font(ui_enums.DEFAULT_FONT, ui_enums.DEFAULT_FONT_SIZE)
        self.srf = self.fnt.render(text, 1, color)
        self.color = color
        self.location = location

    def change_text(self, text, btm):
        dims = (self.srf.get_width(), self.srf.get_height())
        ui_cover_up(self.location, dims, btm)
        self.srf = self.fnt.render(text, 1, self.color)
        self.draw(util.enums.SCREEN)


class UIBox(UIElement):
    def __init__(self, loc, sub_img, upgrade_box=False):
        UIElement.__init__(self, util.enums.RES + "icons/towerbox.png", loc)
        self.subImg = image.load(util.enums.RES + sub_img).convert_alpha()
        self.upgrade = upgrade_box
        if upgrade_box:
            self.subImg = transform.smoothscale(self.subImg, (37, 32))

        if upgrade_box:
            self.sub_loc = (5, 5)
        else:
            self.sub_loc = (7, 8)

        self.draw_subimg()

    def draw_subimg(self):
        self.srf.blit(self.subImg, self.sub_loc)

    def update_subimage(self, subimg):
        self.subImg = image.load(util.enums.RES + subimg).convert_alpha()
        if self.upgrade:
            self.subImg = transform.smoothscale(self.subImg, (37, 32))
        else:
            self.subImg = transform.smoothscale(self.subImg, (37, 32))
        self.draw_subimg()