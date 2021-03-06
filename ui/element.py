from interfaces import UIElement, UIBox
import util.enums as enums


class Heart(UIElement):

    FULL = "full"
    HALF = "half"
    EMPTY = "empty"

    def __init__(self, loc, state="full"):
        self.state = state
        file = enums.RES + "icons/heart.png"
        if state == Heart.HALF:
            file = enums.RES + "icons/halfheart.png"
        elif state == Heart.EMPTY:
            file = enums.RES + "icons/emptyheart.png"
        UIElement.__init__(self, file, loc)

    def set_heart(self, state):
        if state == Heart.HALF:
            file = enums.RES + "icons/halfheart.png"
        elif state == Heart.EMPTY:
            file = enums.RES + "icons/emptyheart.png"
        elif state == Heart.FULL:
            file = enums.RES + "icons/heart.png"
        self.state = state
        self.update_element(file, False)

    def get_heart(self):
        return self.state


class UpgradeBox(UIBox):
    def __init__(self, loc, sub_img):
        UIBox.__init__(self, loc, sub_img, upgrade_box=True)

    def update_box(self, img_path):
        self.update_element(img_path, btm=True)


class TowerBox(UIBox):
    def __init__(self, loc, sub_img):
        UIBox.__init__(self, loc, sub_img, upgrade_box=False)

    def update_box(self, img_path):
        self.update_element(img_path, btm=False)
