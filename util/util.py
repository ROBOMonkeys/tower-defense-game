import ui.enums as enums
from pygame import image
from os import listdir

def add_path(new_path):
    if type(new_path) == tuple:
        for path in new_path:
            if type(new_path) == str:
                path = image.load(path).convert_alpha()
            enums.PATHS.append(path)
    else:
        enums.PATHS.append(new_path)

def add_all_paths():
    for file in listdir(enums.RESOURCES):
        if file.split(".")[0][:-1] == "path":
            add_path(enums.RESOURCES + file)
        
def set_current_map(new_map):
    enums.CUR_MAP = new_map

def add_map(new_map):
    if type(new_map) == tuple:
        for nmap in new_map:
            if type(new_path) == str:
                path = image.load(path).convert_alpha()
            enums.MAPS.append(nmap)
    else:
        enums.MAPS.append(new_map)

def add_all_maps():
    for file in listdir(enums.RESOURCES):
        if file.split(".")[0][:-1] == "map":
            add_map(enums.RESOURCES + file)    

def get_current_map():
    return enums.MAPS[enums.CUR_MAP]
