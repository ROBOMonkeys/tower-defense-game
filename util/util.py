import ui.enums as enums

def add_path(new_path):
    if type(new_path) == tuple:
        for path in new_path:
            enums.PATHS.append(path)
    else:
        enums.PATHS.append(new_path)

def set_current_map(new_map):
    enums.CUR_MAP = new_map

def add_map(new_map):
    if type(new_map) == tuple:
        for nmap in new_map:
            enums.MAPS.append(nmap)
    else:
        enums.MAPS.append(new_map)

def get_current_map():
    return enums.MAPS[enums.CUR_MAP]
