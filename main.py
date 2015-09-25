#!/bin/env python2

# TODO: grid based map system

import pygame
from sys import argv, exit
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_q
from pygame import image, time, mouse
from ui.button import ImageButton, TextButton
from ui.menu import Menu
import ui.enums as ui_enums
import util.enums as enums
from util.util import add_all_paths, add_all_maps, set_current_map, get_current_map, use_test_res
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

pygame.init()

if argv[1] == "test":
    use_test_res()

screen = pygame.display.set_mode((enums.DEFAULT_WIDTH, enums.DEFAULT_HEIGHT))
# monkey = pygame.image.load(enums.RES + 'monkey.png').convert_alpha()

add_all_paths()
add_all_maps()

scanner.scan_map()

running = True

clk = time.Clock()

bg = get_current_map()

screen.blit(bg, (0, 0))
# screen.blit(monkey, (300, 300))
pygame.display.update()

if argv[1] == "buttons":
    buttons = [ImageButton(enums.RES + 'ok_button.png', (300, 200), test),
               TextButton("Start", (300, 100), (0, 0, 0), callback=test)]

    for btn in buttons:
        btn.draw(screen)
elif argv[1] == "menu":
    buttons = False
    mn1 = Menu(("Amazing Cool Game!", (250, 200)),
               ("Start", "Options", "Quit"),
               ((310, 300),
                (310, 340),
                (310, 380)),
               (start_game, open_options, quit_game),
               bg_img=enums.RES + "main_menu.png")
    
    mn1.draw(screen)
elif argv[1] == "scan":
    btn = TextButton("Print Grid",
                     (100, 200),
                     (255, 0, 0),
                     callback=print_grid)
    btn2 = TextButton("Print Grid Length",
                      (200, 200),
                      (255, 0, 0),
                      callback=print_grid_len)
    btn2.draw(screen)
    btn.draw(screen)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_q:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            b1, b2, b3 = mouse.get_pressed()
            if b1:
                enums.CUR_MAP += 1
                if enums.CUR_MAP >= len(enums.MAPS):
                    enums.CUR_MAP = 0
                screen.blit(enums.MAPS[enums.CUR_MAP], (0, 0))
                scanner.scan_map()
                if argv[1] == "scan":
                    btn.draw(screen)
                    btn2.draw(screen)
            else:
                btn.click()
                btn2.click()
    pygame.display.update()
    clk.tick(60)

pygame.quit()
