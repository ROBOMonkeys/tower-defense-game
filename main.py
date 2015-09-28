#!/bin/env python2

# TODO: grid based map system

import pygame
from sys import argv, exit
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, \
    K_DOWN, K_UP, K_LEFT, K_RIGHT, K_q
from pygame import image, time, mouse
from ui.button import ImageButton, TextButton
from ui.interfaces import UIElement, UIString
from ui.menu import Menu
import ui.enums as ui_enums
import util.enums as enums
from util.util import add_all_paths, add_all_maps, \
    set_current_map, get_current_map, use_test_res, \
    map_cover_up
from sprites.interfaces import Creature
import util.scanner as scanner


def test():
    print('okay')


def print_grid():
    for i in range(len(enums.MAP_GRID)):
        print enums.MAP_GRID[i]


def print_grid_len():
    print len(enums.MAP_GRID)
    prin_str = ""
    for i in range(len(enums.MAP_GRID)):
        num_ones = 0
        for j in range(len(enums.MAP_GRID[i])):
            if enums.MAP_GRID[i][j]:
                num_ones += 1
        prin_str += str(i) + ":" + str(num_ones) + ", "
    print prin_str


def start_game():
    print('game started')


def open_options():
    print('options opened')


def quit_game():
    global running
    running = False

if len(argv) < 2:
    print("python2 main.py menu (or buttons)")
    exit(1)


c = None

if argv[1] == "test":
    use_test_res()
    pygame.mixer.init()
    pygame.mixer.music.load(enums.RES + "music/chee-zee-jungle.ogg")
    pygame.mixer.music.play(-1)
    pygame.init()
    global c
    c = Creature((image.load(enums.RES + "monkey.png")))

enums.SCREEN = pygame.display.set_mode((enums.DEFAULT_WIDTH,
                                        enums.DEFAULT_HEIGHT))

add_all_paths()
add_all_maps()

scanner.scan_map()

running = True

clk = time.Clock()

bg = get_current_map()

enums.SCREEN.blit(bg, (0, 0))

pygame.display.update()

if argv[1] == "buttons":
    buttons = [ImageButton(enums.RES + 'ok_button.png', (300, 200), test),
               TextButton("Start", (300, 100), (0, 0, 0), callback=test)]

    for btn in buttons:
        btn.draw(enums.SCREEN)
elif argv[1] == "menu":
    buttons = False
    mn1 = Menu(("Amazing Cool Game!", (250, 200)),
               ("Start", "Options", "Quit"),
               ((310, 300),
                (310, 340),
                (310, 380)),
               (start_game, open_options, quit_game),
               bg_img=enums.RES + "main_menu.png")
    mn1.draw(enums.SCREEN)
elif argv[1] == "scan":
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
    org1 = UIElement(enums.RES + "icons/orangebox1.png", (768, 0))
    org2 = UIElement(enums.RES + "icons/orangebox2.png", (0, 575))
    bananas = UIElement(enums.RES + "icons/pixelbananabunch.png",
                        ui_enums.BUNCH_LOC)
    gear = UIElement(enums.RES + "icons/gear.png",
                     ui_enums.GEAR_LOC)
    clicked = 0
    bunch_cntr = UIString(": " + str(clicked), (60, 589))
    gear_cntr = UIString(": 0", (60, 639))
    org1.draw(enums.SCREEN)
    org2.draw(enums.SCREEN)
    bananas.draw(enums.SCREEN)
    gear.draw(enums.SCREEN)
    bunch_cntr.draw(enums.SCREEN)
    gear_cntr.draw(enums.SCREEN)
    for locs in ui_enums.HEART_LOCS:
        for loc in locs:
            hearts.append(UIElement(enums.RES + "icons/heart.png", loc))
    for heart in hearts:
        heart.draw(enums.SCREEN)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                c.move_left()
            elif event.key == K_RIGHT:
                c.move_right()
            elif event.key == K_UP:
                c.move_up()
            elif event.key == K_DOWN:
                c.move_down()
            elif event.key == K_q:
                quit_game()
        elif event.type == MOUSEBUTTONDOWN:
            b1, b2, b3 = mouse.get_pressed()
            if b1:
                enums.CUR_MAP += 1
                if enums.CUR_MAP >= len(enums.MAPS):
                    enums.CUR_MAP = 0
                enums.SCREEN.blit(enums.MAPS[enums.CUR_MAP], (0, 0))
                scanner.scan_map()
                if argv[1] == "scan":
                    btn.draw(enums.SCREEN)
                    btn2.draw(enums.SCREEN)
                elif argv[1] == "ui":
                    clicked += 1
                    bunch_cntr.update_text(":  " + str(clicked), True)
                    hearts[-(clicked % len(hearts))].update_element(enums.RES + "icons/emptyheart.png", False)
            elif b3:
                btn.click()
                btn2.click()
    if c is not None:
        c.draw(enums.SCREEN)
    pygame.display.update()
    clk.tick(60)

pygame.quit()
