from Source import Source
import pygame



class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image, self.rect = Source.LoadImage('cloud.png', int(9 * Source.height / 42), 30, -1)
        self.speed = 2
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1 * self.speed, 0]

    def draw(self):
        Source.screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


class Star(pygame.sprite.Sprite):
    ni = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = Source.LoadSpriteSheet('star_war.png', 2, 1, 150, 150, -1)
        self.speed = 1
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1 * self.speed, 0]
        self.image = self.images[Star.ni % 2]

    def draw(self):
        Source.screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()
            Star.ni += 1


class Scoreboard():
    def __init__(self, x=-1, y=-1):
        self.score = 0
        self.tempimages, self.temprect = Source.LoadSpriteSheet('numbers.png', 12, 1, 11, int(11 * 6 / 5), -1)
        self.image = pygame.Surface((55, int(11 * 6 / 5)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = Source.width * 0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = Source.height * 0.1
        else:
            self.rect.top = y

    def draw(self):
        Source.screen.blit(self.image, self.rect)

    def update(self, score):
        score_digits = Source.ExtractDigits(score)
        self.image.fill(Source.background_col)
        for s in score_digits:
            self.image.blit(self.tempimages[s], self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0
