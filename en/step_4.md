## Displaying an image

To display an image in Pygame, you first need to load the image. You can start with the Spot the Difference image.

--- task ---
Add in a line to load the image. It can go  above the `pygame.quit()` line.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 12
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
The image may be too big or small for your monitor, so the next step is to scale it using the `width` and `height` variables you created earlier.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 13
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
	
These lines have just loaded the image into the Computer's memory. To display them on the screen, you need to `blit` the image onto the window, and then update the display to show it.

--- task ---
Add the lines shown below to `blit` the image and then update the display.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 15,16, 18
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
	
These linee blits the image to the coordinates `x = 0` and `y = 0`; that is, the top-left corner of the image is being placed in the top-left corner of the window. Then the program sleeps for a few seconds so you can view the image.

