## Switching images

To switch the image to the scary one, you need to add a pause and then re-blit another image.

--- task ---
First, you load the scary image into memory and scale it in the same way you did before with the `difference` image.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 15,16
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

zombie = pygame.image.load('scary_face.png')
zombie = pygame.transform.scale(zombie, (width, height))

screen.blit(difference, (0, 0))
pygame.display.update()

sleep(3)

pygame.quit()
--- /code ---
--- /task ---

--- task ---
Then you can `blit` the newimage to the display, and update the display.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 23,24
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

zombie = pygame.image.load('scary_face.png')
zombie = pygame.transform.scale(zombie, (width, height))

screen.blit(difference, (0, 0))
pygame.display.update()

sleep(3)

screen.blit(zombie, (0,0))
pygame.display.update()

pygame.quit()
--- /code ---
--- /task ---

--- task ---
Save and run the program again, to see the new image being placed.
--- /task ---

--- task ---
It's a little predictable at the moment, so you can add some randomness by changing the `sleep` time between the two images to a random number.
--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 21
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

zombie = pygame.image.load('scary_face.png')
zombie = pygame.transform.scale(zombie, (width, height))

screen.blit(difference, (0, 0))
pygame.display.update()

sleep(randrange(5,15))

screen.blit(zombie, (0,0))
pygame.display.update()

pygame.quit()
--- /code ---
--- /task ---

--- task ---
Save and run your code again, to see if the random sleep is working
--- /task ---
