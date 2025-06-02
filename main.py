import pygame
import os
import pgzrun

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

HEIGHT = 1200
WIDTH = 2000

raindrop = pygame.image.load('images/raindrop.png')
scaled_raindrop = pygame.transform.scale(raindrop, (100, 100))
pygame.image.save(scaled_raindrop, 'images/raindrop.png')

raindrop = Actor("raindrop.png")

def draw():
    pass

pgzrun.go()