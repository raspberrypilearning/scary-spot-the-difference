## Switch images

To switch the image to the scary one, you need to use `blit` again.

--- task ---
First load the scary image into memory and scale it, in the same way as the `difference` image.

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
Now add two new lines to prepare the window for displaying the new image, and then update the display.

--- hints --- --- hint ---
You need to use the `screen.blit()` command with a file name.
--- /hint --- --- hint ---
Here are the lines of code you need to add:
```python
screen.blit(zombie, (0,0))
pygame.display.update()
```

--- /hint --- --- hint ---
Here is the full code:

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
--- /hint --- --- /hints ---
--- /task ---

--- task ---
Save and run the program again to see the new image being displayed.
--- /task ---