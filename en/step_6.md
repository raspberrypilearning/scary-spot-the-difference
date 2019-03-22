## Making it random

It's a little predictable at the moment, so you can add some randomness by changing the `sleep` time between the two images to a random number.

--- task ---
Change the time between the two images being on screen to a random number.



--- hints --- --- hint ---
You have imported the `randrange` function at the top of your program. Can you use this function to select a random time?
--- /hint --- --- hint ---
Here is the line you'll need to add in:

```python
sleep(randrange(5,15))
```
--- /hint --- --- hint ---
Here is the full code:

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
hint 3 title
--- /hint --- --- /hints ---


