# -*- coding: utf-8 -*-
"""
This is a platformer game based on keyboard contol for our Software Design project.

@author: Skye Ozga, Mason Grabowski, Jerry Goss, Jamie Santiago
"""

import time
import pygame, sys
import avatar, platform2, stage
from entity import Entity, DynamicEntity
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

    started = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            if controller.handle_keys(pygame.key.get_pressed()):
                started = True

        if started:
            if not model.dead:
                if not model.stage().completed:
                    if model.update() == 'QUIT':
                        running = False
                    view.draw()
                    time.sleep(.001)
                else:
                    view.screen.blit(pygame.image.load('victory.png'),(0,0))
                    pygame.display.update()
                    time.sleep(.1)
                    if controller.handle_keys(pygame.key.get_pressed()):
                        model.reset()
            else:
                view.screen.blit(pygame.image.load('death-screen.png'),(0,0))
                pygame.display.update()
                time.sleep(.1)
                if controller.handle_keys(pygame.key.get_pressed()):
                    model.reset()
        else:
            view.screen.blit(pygame.image.load('title-screen.png'),(0,0))
            pygame.display.update()
            time.sleep(.1)



    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    size = (1920, 1080)
    start_game(size)
