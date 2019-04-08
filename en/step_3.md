##	Set up your prank

Your first step is to display the `spot-the-diff.png` image on the screen. To do this, you need the computer to detect the size of your monitor. You need to know the monitor size because different types of monitors have different resolutions, and you need to know the resolution to display the image correctly.

--- task ---
Create two new variables called `width` and `height`. Then use the `display.Infor()` methods to find out the width and height of your monitor.

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
Now tell Pygame to create a large window in which the game can be played. Then get Pygame to quit.

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

Save your program and then run it. You should see a blank rectangular window open. This is the Pygame window. It should close itself straight away, because your program reaches the `pygame.quit()` line.
--- /task ---



