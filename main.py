from gameplay import Gameplay
import pygame

pygame.init()
pygame.display.set_caption("Dino Run ")


def main():
    isGameQuit = Gameplay.introscreen()
    if not isGameQuit:
        Gameplay.gameplay()


main()
