import pygame
import random
from Source import Source


class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = Source.LoadSpriteSheet('cacti-vec-prob-5.png', 1, 10, sizex, sizey, -1)
        self.rect.bottom = int(0.98 * Source.height)
        self.rect.left = Source.width + self.rect.width
        self.image = self.images[random.randrange(0, 10)]
        self.movement = [-1 * speed, 0]

    def draw(self):
        Source.screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()


class Ptera(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = Source.LoadSpriteSheet('ptera.png', 2, 1, sizex, sizey, -1)
        self.ptera_height = [Source.height * 0.82, Source.height * 0.75, Source.height * 0.60]
        self.rect.centery = self.ptera_height[random.randrange(0, 3)]
        self.rect.left = Source.width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        Source.screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)
        if self.rect.right < 0:
            self.kill()
