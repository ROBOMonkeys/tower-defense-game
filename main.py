#!/bin/env python2

# TODO: grid based map system

from sys import argv
from os import path

import pygame
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_q, K_ESCAPE
from pygame import image, time, mouse

from ui.button import ImageButton, TextButton
from ui.interfaces import UIString, UIElement
from ui.element import Heart
from ui.menu import Menu
import ui.enums as ui_enums
from ui import ui_util

import util.enums as enums
from util.util import add_all_paths, add_all_maps, \
    get_current_map, use_test_res
import util.scanner as scanner

from test import *

from sprites.interfaces import Robot, Group


def quit_game():
    global running
    running = False

enums.RES = path.dirname(path.realpath(__file__)) + "/res/"

c = None

pygame.init()
enums.SCREEN = pygame.display.set_mode((enums.DEFAULT_WIDTH,
                                        enums.DEFAULT_HEIGHT))

add_all_paths()
add_all_maps()
scanner.scan_map()

bg = get_current_map()
enums.SCREEN.blit(bg, (0, 0))
pygame.display.update()

if len(argv) > 1:
    if argv[1] == "test":
        use_test_res()
        pygame.mixer.init()
        pygame.mixer.music.load(enums.RES + "music/chee-zee-jungle.ogg")
        pygame.mixer.music.play(-1)
        global c
        c = Robot((image.load(enums.RES + "monkey.png")))
        if argv[2] == "buttons":
            buttons = [ImageButton(enums.RES + 'ok_button.png', (300, 200), test),
                       TextButton("Start", (300, 100), (0, 0, 0), callback=test)]

            for btn in buttons:
                btn.draw(enums.SCREEN)
        elif argv[2] == "menu":
            buttons = False
            mn1 = Menu(("Amazing Cool Game!", (250, 200)),
                       ("Start", "Options", "Quit"),
                       ((310, 300),
                        (310, 340),
                        (310, 380)),
                       (start_game, open_options, quit_game),
                       bg_img=enums.RES + "main_menu.png")
            mn1.draw(enums.SCREEN)

    if argv[1] == "scan":
        btn = TextButton("Print Grid",
                         (100, 200),
                         (255, 0, 0),
                         callback=print_grid)
        btn2 = TextButton("Print Grid Length",
                          (200, 200),
                          (255, 0, 0),
                          callback=print_grid_len)
        btn2.draw(enums.SCREEN)
        btn.draw(enums.SCREEN)
    elif argv[1] == "ui":
        hearts = []
        org1 = UIElement(enums.RES + "icons/orangebox4.png", (768, 0))
        org2 = UIElement(enums.RES + "icons/orangebox3.png", (0, 575))
        bananas = UIElement(enums.RES + "icons/pixelbananabunch.png",
                            ui_enums.BUNCH_LOC)
        gear = UIElement(enums.RES + "icons/gear.png",
                         ui_enums.GEAR_LOC)
        clicked = 0
        bunch_cntr = UIString(": " + str(clicked), (60, 589))
        gear_cntr = UIString(": 0", (60, 639))

        btn_srf = image.load(enums.RES + "icons/towerbox.png").convert_alpha()
        ui_util.blit_subsurface(btn_srf,
                                image.load(enums.RES + "towers/proj_0_p.png").convert_alpha(),
                                (5, 5),
                                resize=True,
                                size=(37, 39))
        btn = ImageButton(btn_srf,
                          ui_enums.TOWER_LOCS[0],
                          make_new_proj_tower)
        del btn_srf
        org1.draw(enums.SCREEN)
        org2.draw(enums.SCREEN)
        bananas.draw(enums.SCREEN)
        gear.draw(enums.SCREEN)
        bunch_cntr.draw(enums.SCREEN)
        gear_cntr.draw(enums.SCREEN)
        btn.draw(enums.SCREEN)
        for locs in ui_enums.HEART_LOCS:
            for loc in locs:
                hearts.append(Heart(loc))
scanner.scan_map()
enums.SPRITES.append(Group())
enums.BG = enums.SCREEN.copy()

running = True
clk = time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_q:
                quit_game()
        elif event.type == MOUSEBUTTONDOWN:
            b1, b2, b3 = mouse.get_pressed()
            if b1:
                if argv[1] == "ui":
                    clicked += 1
                    bunch_cntr.change_text(":  " + str(clicked), True)
                    heart = hearts[-(clicked % len(hearts))]
                    if heart.get_heart() == Heart.FULL:
                        heart.set_heart(Heart.HALF)
                    elif heart.get_heart() == Heart.HALF:
                        heart.set_heart(Heart.EMPTY)
                    else:
                        heart.set_heart(Heart.FULL)
                    if b2:
                        for t in enums.SPRITES[0]:
                            t.upgrade()
                    if b3:
                        for t in enums.SPRITES[0]:
                            t.set_state(3)
                    btn.update()
    for heart in hearts:
        heart.update()
    if len(enums.SPRITES) > 0:
        enums.SPRITES[0].update()
    if c is not None:
        c.draw(enums.SCREEN)
    pygame.display.update()
    clk.tick(60)

pygame.quit()
