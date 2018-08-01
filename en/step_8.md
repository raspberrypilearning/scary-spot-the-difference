## Adding some sound

- Now it's time to add the scream, to make the game a little scarier. In Python, just like you did with the images, the sound needs to be loaded first. You want to do this **before** the second image is displayed. Change your code so it looks like this:

    ``` python
	zombie = pygame.transform.scale(zombie, (width, height))

	scream = pygame.mixer.Sound("scream.wav")
	
	sleep(randrange(5,15))
    ```

- Then, you want to start playing the sound just before the second image is shown, as soon as the sleep has finished.

    ``` python
    scream.play()
    ```

- Next, stop the scream just before Pygame quits:

    ``` python
    scream.stop()
    pygame.quit()
    ```

- You might find that, depending on your Raspberry Pi model, the scream takes a little time to start playing. You could, therefore, add a little sleep just after the `scream.play()` line.

Your complete code should look like this:

```python	
import pygame
from pygame.locals import*
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height))

difference = pygame.image.load('spot_the_diff.png')
difference = pygame.transform.scale(difference, (width, height))

screen.blit(difference, (0,0))
pygame.display.update()

zombie = pygame.image.load('scary_face.png')
zombie = pygame.transform.scale(zombie, (width, height))

scream = pygame.mixer.Sound("scream.wav")

sleep(randrange(5,15))

scream.play()
sleep(0.4)
screen.blit(zombie, (0,0))
pygame.display.update()

sleep(3)
scream.stop()
pygame.quit()
	
```
	
