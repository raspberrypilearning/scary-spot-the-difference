## Display an image

To display an image in Pygame, you first need to load the image. Start with the `spot_the_diff.png` image.

--- task ---
Add a line of code to load the image. Put the new line above the `pygame.quit()` line.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 1
line_highlights: 12
---
import pygame
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))

difference = pygame.image.load('spot_the_diff.png')

pygame.quit()
--- /code ---
--- /task ---

--- task ---
The image may be too big or small for your monitor. Your next step is to scale the image using the `width` and `height` variables.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 1
line_highlights: 13
---
import pygame
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))

difference = pygame.image.load('spot_the_diff.png')
difference = pygame.transform.scale(difference, (width, height))

pygame.quit()
--- /code ---
--- /task ---
	
These new lines of code only load the image into your computer's memory. Now use the command `blit` to prepare the Pygame window to display the image. Then update the display to show the image.

--- task ---
Add the new lines shown below to prepare the Pygame window using `blit`, and to then update the display.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
line_highlights: 15,16, 18
---
import pygame
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))

difference = pygame.image.load('spot_the_diff.png')
difference = pygame.transform.scale(difference, (width, height))

screen.blit(difference, (0, 0))
pygame.display.update()

sleep(3)

pygame.quit()
--- /code ---
--- /task ---
	
These lines display the image at the coordinates `x = 0` and `y = 0`. This means the top left-hand corner of the images is placed in the top left-hand corner of the window. Then the program sleeps for a few seconds so you can view the image.

