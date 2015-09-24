import ui.enums as enums

def compare_surfaces(srf_ref, srf_cmp):
    x, y = srf_ref.get_size()
    for w in range(x):
        for h in range(y):
            if not srf_ref.get_at((w,h)) == srf_cmp.get_at((w,h)):
                return False
    return True

def scan_map():
    print enums.PATHS, enums.MAPS
    cur = enums.MAPS[enums.CUR_MAP]
    for h in range(cur.get_height() / enums.TILE_H):
        for w in range(cur.get_width() / enums.TILE_W):
            for path in enums.PATHS:
                if compare_surfaces(path, cur.subsurface(w * enums.TILE_W,
                                                         h * enums.TILE_H,
                                                         enums.TILE_H,
                                                         enums.TILE_W)):
                    print "dirt ID'd at x:" + str(w * enums.TILE_W) + ", y:" + str(h * enums.TILE_H)
