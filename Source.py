import pygame
from pygame import *
import os
pygame.mixer.init()

scr_size = (width,height) = (600,300)
FPS = 60
gravity = 0.6
ni = 0
si = 0

background_col = (235,235,235)

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Run ")

jump_sound = pygame.mixer.Sound('sprites/jump_3.wav')
die_sound = pygame.mixer.Sound('sprites/die_3.wav')
checkPoint_sound = pygame.mixer.Sound('sprites/checkpoint_3.wav')
duck_sound = pygame.mixer.Sound('sprites/duck_1.wav')

dino_skin = ['dinos.png', 'dinoz.png', 'dinok.png']
dino_ducking_skin = ['dinos_ducking.png', 'dinoz_ducking.png', 'dinok_ducking.png']

def LoadImage(name,sizex,sizey,colorkey,):
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey, RLEACCEL)
    image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

def LoadSpriteSheet(sheetname,nx,ny,scalex,scaley,colorkey,):
    fullname = os.path.join('sprites',sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey == -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,RLEACCEL)


            image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect

def DispGameOverMsg(retbutton_image, gameover_image):
    retbutton_rect = retbutton_image.get_rect()
    retbutton_rect.centerx = width / 2
    retbutton_rect.top = height*0.52

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2
    gameover_rect.centery = height*0.35

    screen.blit(retbutton_image, retbutton_rect)
    screen.blit(gameover_image, gameover_rect)

def ExtractDigits(number):
    if number > -1:
        digits = []
        i = 0
        while(number > 0):
            digits.append(number%10)
            number = int(number/10)
        for i in range(len(digits),5):
            digits.append(0)
        digits.reverse()
        return digits