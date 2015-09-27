#!/bin/env python2

# TODO: grid based map system

import pygame
from sys import argv, exit
from pygame.locals import QUIT, KEYDOWN, MOUSEBUTTONDOWN, K_q
from pygame import image, time
from ui.button import ImageButton, TextButton
from ui.menu import Menu
import ui.enums as enums
from util.util import add_all_paths, add_all_maps, set_current_map, get_current_map, use_test_res
import util.scanner as scanner

def test():
    print('okay')


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
#monkey = pygame.image.load(enums.RES + 'monkey.png').convert_alpha()

add_all_paths()
add_all_maps()

scanner.scan_map()

running = True

clk = time.Clock()

bg = get_current_map()

screen.blit(bg, (0, 0))
#screen.blit(monkey, (300, 300))
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
else:
    pass

pygame.mixer.init()
pygame.mixer.music.load(enums.RES + "music/jungle-test.ogg")
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_q:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            enums.CUR_MAP += 1
            if enums.CUR_MAP >= len(enums.MAPS):
                enums.CUR_MAP = 0
            screen.blit(enums.MAPS[enums.CUR_MAP], (0,0))
            scanner.scan_map()
    pygame.display.update()
    clk.tick(60)

pygame.quit()
