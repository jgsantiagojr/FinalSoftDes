import pygame

class Weapons(DynamicEntity):
    """docstring for Weapons."""
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return "Weapon x=%f, y=%f, angle=%f" % (self.x, self.y, self.angle)

class Gun(Weapons):
    """Projectile based wepaon"""
    def __init__(self, x, y, angle):
        super(Gun, self).__init__(x, y, angle)

    def attack(self, bullets):
        ##creates a bullet
        bullets.append(bullet(x, y, angle))

class Shuriken(Weapons):
    """Projectile based weapon"""
    def __init__(self, x, y, angle):
        super(Shuriken, self).__init__(x, y, angle)

    def attack(self, shuriken_list):
        ##creates a shuriken
        shuriken_list.append(shurikens(x,y,angle))
        
    def scatter_throw(self, shuriken_list):
        ##creates 5 shurikens, at varied angles
        shuriken1 = shurikens(x, y, angle + 90)
        shuriken2 = shurikens(x,y, angle + 45)
        shuriken3 = shurikens(x,y, angle)
        shuriken4 = shurikens(x,y, angle - 45)
        shuriken5 = shurikens(x,y, angle - 90)
        
        shuriken_list.append(shuriken1, shuriken2, shuriken3, shuriken4, shuriken5)
        
class Whip(Weapons):
    """Collision based weapon"""
    def __init__(self, x, y, angle):
        super(Gun, self).__init__(x, y, angle)

    def attack(self):
        ##tell the view module to run the whip attack gif with
        ##the hitbox being rewritten around it
        return True

class Sword(Weapons):
    """Collision based weapon"""
    def __init__(self, x, y, angle):
        super(Sword, self).__init__(x, y, angle)

    def attack(self):
        ##tell the view module to run the sword attack gif with
        ##the hitbox being rewritten around it
        return True
    
class Weapons_Inventory(object):
    """Keeps track of what weapons the user has"""
    def __init__(self)
