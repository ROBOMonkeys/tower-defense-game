from pygame import image, font, Surface
from ui.enums import DEFAULT_FONT, DEFAULT_FONT_SIZE
from ui.interfaces import Clickable


class ImageButton(Clickable):
    """
A button class that allows the use of an image as the clickable aspect

Vars:
 img_path = path to image
 loc      = location to display the button
 callback = function to call when the button is clicked, defaults to None
    """

    def __init__(self, img_path, loc, callback=None):
        if type(img_path) == Surface:
            self.srf = img_path
        else:
            self.srf = image.load(img_path).convert_alpha()
        self.location = loc
        self.height = self.srf.get_height()
        self.width = self.srf.get_width()
        self.callback = callback


class TextButton(Clickable):
    """
A button class that allows the use of text as the clickable aspect

Vars:
 text      = text to render
 loc       = location to display the button
 color     = color to display the text
 bg_color  = color for the text background
 callback  = function to call when button is clicked
 fnt       = font to use
 size      = size of text
 bold      = render text bolded
 underline = render text underlined
 italics   = render text italicized
    """

    def __init__(self, text, loc, color=(0, 0, 0), bg_color=None,
                 callback=None, fnt=DEFAULT_FONT, size=DEFAULT_FONT_SIZE,
                 bold=False, underline=False, italics=False):
        
        if not font.get_init():
            font.init()
        self.fnt = font.Font(fnt, size)
        
        self.fnt.set_bold(bold)
        self.fnt.set_underline(underline)
        self.fnt.set_italic(italics)
        
        if bg_color is not None:
            self.srf = self.fnt.render(text, 1, color, bg_color)
        else:
            self.srf = self.fnt.render(text, 1, color)
        
        self.width = self.srf.get_width()
        self.height = self.srf.get_height()
        
        self.location = loc
        self.callback = callback
