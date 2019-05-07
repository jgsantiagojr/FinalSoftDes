"""
Platformer keyboard controller code
"""
import pygame, sys
import pygame.locals

class PyGameKeyboardController(object):
    """ Handles keyboard input for platformer """
    def __init__(self,model):
        # Tells the controller where to send inputs to
        self.model = model

    def handle_keys(self,keys):
        """ Key presses are passed to the model avatar to be handled """
        # Move left if left arrow or a are pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.model.avatar.addinput('LEFT')
        else:
            self.model.avatar.removeinput('LEFT')
        # Move right if right arrow or d are pressed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.model.avatar.addinput('RIGHT')
        else:
            self.model.avatar.removeinput('RIGHT')
        # Move right if right arrow or d are pressed
        if keys[pygame.K_x] or keys[pygame.K_f]:
            self.model.avatar.addinput('ATTACK')
        else:
            self.model.avatar.removeinput('ATTACK')
        # Jump if space, up arrow, or w are pressed
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.model.avatar.addinput('JUMP')
        else:
            self.model.avatar.removeinput('JUMP')
        # Quits the game if q or p are pressed
        if keys[pygame.K_q] or keys[pygame.K_p]:
            self.model.avatar.addinput('QUIT')
        else:
            self.model.avatar.removeinput('QUIT')
        if keys[pygame.K_w] or keys[pygame.K_e] or keys[pygame.K_r] or keys[pygame.K_t] or keys[pygame.K_y] or keys[pygame.K_u] or keys[pygame.K_i] or keys[pygame.K_o] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_f] or keys[pygame.K_g] or keys[pygame.K_h] or keys[pygame.K_j] or keys[pygame.K_k] or keys[pygame.K_l] or keys[pygame.K_z] or keys[pygame.K_x] or keys[pygame.K_c] or keys[pygame.K_v] or keys[pygame.K_b] or keys[pygame.K_n] or keys[pygame.K_m] or keys[pygame.K_1] or keys[pygame.K_2] or keys[pygame.K_3] or keys[pygame.K_4] or keys[pygame.K_5] or keys[pygame.K_6] or keys[pygame.K_7] or keys[pygame.K_8] or keys[pygame.K_9] or keys[pygame.K_0] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_SPACE]:
            return True
