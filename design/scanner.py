from pygame import image, Rect
from ui.enums import TILE_H, TILE_W, RESOURCES, CUR_MAP, PATHS

def compare_surfaces(srf_ref, srf_cmp):
    x, y = srf_ref.get_size()
    for w in range(x):
        for h in range(y):
            if not srf_ref.get_at((w,h)) == srf_cmp.get_at((w,h)):
                return False
    return True

def scan_map():
    for h in range(CUR_MAP.get_height() / TILE_H):
        for w in range(CUR_MAP.get_width() / TILE_W):
            for path in PATHS:
                if compare_surfaces(path, tileset.subsurface(w*TILE_W, h*TILE_H, TILE_H, TILE_W)):
                    print "dirt ID'd at x:" + str(w*32) + ", y:" + str(h*32)
