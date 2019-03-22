##	Displaying an image

The first step will be to display the `spot-the-diff.png` image on the screen. To do this you need the computer to detect the size of your monitor, as they all have different resolutions.

--- task ---
Create two new variables called `width` and `height`. You can use the `display.Infor()` methods to then find out the width and height of your monitor.

--- code ---
---
language: python
filename: scary_spot_the_difference.py
line_numbers: true
line_number_start: 
highlight_lines: 8-9
---
import pygame
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
--- /code ---
--- /task ---

--- task ---
Now you can tell Pygame to create a large window for the game to be played in, and then get Pygame to quit.

--- code ---
---
language: python
filename: scary_spot_the_difference
line_numbers: true
line_number_start: 
highlight_lines: 10, 12
---
import pygame
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))
	
pygame.quit()
--- /code ---

--- /task ---

--- task ---
Save your file again and then run it, and you should see a blank rectangular window open. This is the Pygame window. It should close itself straight away, as your program reaches the `pygame.quit()` line.
--- /task ---



