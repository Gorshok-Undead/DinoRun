import os
import sys
from gameplay import gameplay, introscreen
import pygame

pygame.init()

def main():
    isGameQuit = introscreen()
    if not isGameQuit:
        gameplay()

main()