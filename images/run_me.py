import pygame
from pygame.locals import*
from time import sleep

pygame.init()

scream = pygame.mixer.Sound("scream.wav")
difference = pygame.image.load('Halloween_Spot_the_Diff.png')
angel = pygame.image.load('Scary_Face.png')

white = (255, 255, 255)
w = 1920
h = 1080
screen = pygame.display.set_mode((w, h), FULLSCREEN)

screen.fill((white))
screen.blit(difference, (0,0))
pygame.display.update()
sleep(15)
scream.play()
screen.blit(angel, (0,0))
pygame.display.update()

sleep(3)
scream.stop()
pygame.quit()

