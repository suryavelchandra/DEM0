import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        print("adding vecs " + str(self.vel + self.acc))

    def update(self):
        self.acc = vec(0, 0)
        print("acc " + str(self.acc))
        print("vel " + str(self.vel))

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -0.5
        if keys[pg.K_RIGHT]:
            self.acc.x = 0.5

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.center = self.pos

