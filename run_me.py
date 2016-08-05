import pygame
from pygame.locals import*
from time import sleep

pygame.init()


scream = pygame.mixer.Sound("scream.wav")
difference = pygame.image.load('who.jpg')
angel = pygame.image.load('angel.jpg')

white = (255, 255, 255)
w = 1280
h = 675
screen = pygame.display.set_mode((w, h), FULLSCREEN)
screen.fill((white))

screen.fill((white))
screen.blit(difference, (0,0))
pygame.display.update()
sleep(10)
scream.play()
screen.blit(angel, (0,0))
pygame.display.update()

sleep(3)
scream.stop()
pygame.quit()

