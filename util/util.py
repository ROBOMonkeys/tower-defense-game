import enums
from pygame import image
from os import listdir


def use_test_res():
    enums.RES = enums.TEST_RES


def add_path(new_path):
    if type(new_path) == tuple:
        for path in new_path:
            if type(new_path) == str:
                path = image.load(path).convert_alpha()
            enums.PATHS.append(path)
    else:
        if type(new_path) == str:
            new_path = image.load(new_path).convert_alpha()
        enums.PATHS.append(new_path)


def add_all_paths():
    for file in listdir(enums.RES + "tiles/"):
        if file.split(".")[0][:4] == "path":
            add_path(enums.RES + "tiles/" + file)


def set_current_map(new_map):
    enums.CUR_MAP = new_map


def add_map(new_map):
    if type(new_map) == tuple:
        for nmap in new_map:
            if type(new_map) == str:
                nmap = image.load(nmap).convert_alpha()
            enums.MAPS.append(nmap)
    else:
        if type(new_map) == str:
            new_map = image.load(new_map).convert_alpha()
        enums.MAPS.append(new_map)


def add_all_maps():
    for file in listdir(enums.RES + "maps/"):
        if file.split(".")[0][:3] == "map":
            add_map(enums.RES + "maps/" + file)


def get_current_map():
    return enums.MAPS[enums.CUR_MAP]


def map_cover_up(loc, spr_dim):
    enums.SCREEN.blit(get_current_map().subsurface(loc[0],
                                                   loc[1],
                                                   spr_dim[0],
                                                   spr_dim[1]),
                      loc)


def ui_cover_up(loc, dims, bottom):
    if bottom:
        locs = (768 - loc[0], loc[1] - 576)
        ui_side = image.load(enums.RES + "icons/orangebox2.png").convert()
    else:
        locs = (loc[0] - 768, 576 - loc[1])
        ui_side = image.load(enums.RES + "icons/orangebox1.png").convert()
    enums.SCREEN.blit(ui_side.subsurface(locs[0],
                                         locs[1],
                                         dims[0],
                                         dims[1]),
                      loc)


def build_in_game_ui():
    pass
