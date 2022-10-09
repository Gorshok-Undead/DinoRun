from Source import Source


class Ground:
    def __init__(self, speed=-5):
        self.image, self.rect = Source.LoadImage('ground.png', 600, 20, -1)
        self.image1, self.rect1 = Source.LoadImage('ground.png', 600, 20, -1)
        self.rect.bottom = Source.height
        self.rect1.bottom = Source.height
        self.rect1.left = self.rect.right
        self.speed = speed

    def draw(self):
        Source.screen.blit(self.image, self.rect)
        Source.screen.blit(self.image1, self.rect1)

    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right
