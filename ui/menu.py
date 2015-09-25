from pygame import font, image
from button import TextButton, ImageButton
from ui.enums import Drawable, DEFAULT_FONT, DEFAULT_FONT_SIZE


class MenuText(Drawable):
    """
A class that represents text on a menu

Vars:
 text     = text to display
 loc      = location tuple of where to display the text at
 fnt      = font to use
 size     = font size to use
 color    = color of text
 bg_color = background color of the text
    """
    def __init__(self, text, loc,
                 fnt=DEFAULT_FONT, size=DEFAULT_FONT_SIZE,
                 color=(0, 0, 0), bg_color=None):
        super(type(self), self).__init__()
        
        if not font.get_init():
            font.init()

        self.fnt = font.Font(fnt, size)
        if bg_color is not None:
            self.srf = self.fnt.render(text, 1, color, bg_color)
        else:
            self.srf = self.fnt.render(text, 1, color)
        self.location = loc


class Menu(Drawable):
    """
A Class that describes a menu

Vars:
 title     = a tuple where title[0] is a title string and title[1] is a location tuple
 opts      = tuple of strings of options for the menu
 opts_loc  = tuple of location tuple for the opts
 opts_clbk = tuple of function refs for the opts
 img_btns  = if true then treat opts as image paths and make ImageButtons instead of TextButtons
 bg_img    = path to a background image for the menu
 fnt       = different font to use
 btn_args  = dict that maps to arguments for the TextButton class
    """
    def __init__(self, title, opts, opts_loc, opts_clbk,
                 img_btns=False,
                 bg_img=None, fnt=DEFAULT_FONT, **btn_args):
        super(type(self), self).__init__()
        
        self.srf = []
        self.location = None
        if bg_img is not None:
            self.srf.append(image.load(bg_img))
            self.location = (0, 0)

        self.srf.append(MenuText(title[0], title[1]))

        if img_btns:
            btn = ImageButton
        else:
            btn = TextButton
            
        i = 0
        while i < len(opts):
            self.srf.append(btn(opts[i], opts_loc[i],
                                callback=opts_clbk[i]))
            i += 1

    def handle_clicks(self):
        """
        Handles the clicks for the menu
        """
        for btn in self.srf:
            if btn.__class__.__name__ == "TextButton" or \
               btn.__class__.__name__ == "ImageButton":
                btn.click()
