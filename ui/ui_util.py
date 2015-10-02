from pygame import transform


def blit_subsurface(parent_srf, child_srf, loc, resize=False, size=None):
    if resize:
        child_srf = transform.smoothscale(child_srf, size)
    parent_srf.blit(child_srf, loc)


def build_in_game_ui():
    pass
