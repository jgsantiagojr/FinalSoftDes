# -*- coding: utf-8 -*-
"""
This is a platformer game based on keyboard contol for our Software Design project.

@author: Michael Remley and Skye Ozga
"""

import time
import pygame, sys
import avatar, platform, stage
from model import PlatformerModel
from view import PyGameWindowView
from keyboard_controller import PyGameKeyboardController


def start_game(size):
    """
    Given screen 'size' as (x,y) tuple, start platformer game
    """
    pygame.init()
    pygame.key.set_repeat(50,1)
    clock = pygame.time.Clock()
    model = PlatformerModel(size, clock)
    print(model)
    view = PyGameWindowView(model, size)
    controller = PyGameKeyboardController(model)


    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.locals.QUIT:
                running = False
            if controller.handle_keys(pygame.key.get_pressed()):
                running = False

        if model.update():
            running = False
        view.draw()

        time.sleep(.001)

    pygame.quit()
    sys.exit

if __name__ == '__main__':
    size = (1920, 1080)
    start_game(size)
