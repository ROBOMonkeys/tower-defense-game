from pygame import image
from interfaces import Drawable


class UIElement(Drawable):
    def __init__(self, img_path, location):
        self.srf = image.load(img_path)
        self.location = location
