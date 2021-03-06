import pygame, math
from pygame import Vector2
from entity import Entity, DynamicEntity
from bullets import Projectile, Bullet, Shuriken

class StaticEnemy(Entity):

    def __init__(self, x, y, images, bullet_images):
        super().__init__(x, y, images)
        self.bullet_images = bullet_images

        self.health = 1
        self.clock = 0
        self.cooldown = 750

        self.handpos = Vector2(x, y)
        self.trajectory = Vector2(1,0)


    def aim(self, avatar, stage):
        target = Vector2(avatar.x, avatar.y)
        platforms = stage.platforms

        trajectory = Vector2(target - self.handpos)
        self.trajectory = trajectory/trajectory.length()

        testpoint = Vector2(self.handpos)
        stepsize = 10

        while stage.contains_point(testpoint):
            for p in stage.platforms:
                if p.contains_point(testpoint):
                    return False
                elif avatar.contains_point(testpoint):
                    return True


            testpoint += stepsize * self.trajectory

        return False

    def shoot(self, dt):
        self.clock += dt
        if self.clock > self.cooldown:
            self.clock = self.clock % self.cooldown
            return True
        return False

    def update(self, avatar, stage, enemy_projectiles: pygame.sprite.Group, dt):
        super().update()
        if self.clock < 300:
            self.frame = int(self.frame%2 + 2 + 2*((self.clock)//100))
        if self.aim(avatar, stage):
            if self.clock > 300:
                if self.trajectory.dot(Vector2(1,0)) > 0:
                    self.frame = 1
                else:
                    self.frame = 0
            if self.shoot(dt):
                enemy_projectiles.add(Bullet(self.handpos.x, self.handpos.y, self.trajectory, self.bullet_images))
