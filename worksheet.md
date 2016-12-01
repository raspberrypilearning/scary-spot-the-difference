# Scary Spot the Difference - Python

In this resource you will make a Spot the Difference game with a difference! While the player is focused intently on the screen trying to figure out the difference between two images, they'll have no idea they're about to receive the fright of their life.

If you would like to make this project using Scratch instead of Python, head over to the [Scratch worksheet](worksheet2.md).

## Gathering the assets

1. You're going to need two images and a sound file for this activity. Firstly, you'll need a Spot the Difference image. This one is free to use, but you can make or find your own if you prefer.

   ![image](images/spot_the_diff.png)

1. Next, you'll need the image you're going to swap out to give them a fright. This zombie face is cool, but you can make or find your own if you like. Just remember the age of the people you're trying to scare and choose something appropriate.

	![image](images/scary_face.png)

1. Lastly, you'll need a scary sound to really give them a fright. You can download [this one](http://soundbible.com/1627-Female-Scream-Horror.html), which should do the trick. Make sure you download the `wav` version of the file, or again find your own. Once you have the file, rename it to `scream.wav`.

1. Save all the files in a single directory, where your Python script will be.

## Setting up your file

1. Open IDLE by clicking on Menu> Programming > Python 3 (IDLE), then click File and New File.

1. Save your file straight away, in the same directory as your images. If you call it `run_me.py`, you won't be giving the game away to your victim.

1. To begin with, you'll need to import the Pygame library and some of its modules. You're also going to need the `sleep` and `randrange` functions.

    ``` python
    import pygame
    from pygame.locals import*
	from time import sleep
	from random import randrange
    ```
	
1. Next, you need to initialise Pygame so that it's ready to be used. As different monitors have different sizes, you need to find out the width and height of your monitor, and save them as variables.

    ``` python
	pygame.init()

	width = pygame.display.Info().current_w
	height = pygame.display.Info().current_h
	```
    
1. Lastly for this section, you can instruct Pygame to create a full-screen window for the game to be played in, and then get Pygame to quit.

    ``` python
	screen = pygame.display.set_mode((width, height), FULLSCREEN)
	
	pygame.quit()
    ```

1. Save your file again and then run it by pressing `F5`.

1. You should see a blank rectangular window open. This is the Pygame window. It should close itself straight away, as your program reaches the `pygame.quit()` line.

## Displaying an image

1. To display an image in Pygame, you first need to load the image. You can start with the Spot the Difference image. Place this line above the `pygame.quit()` line. If you've used a different image, don't forget to change the name.

	``` python
	difference = pygame.image.load('spot_the_difference.png')
	```

1. The image may be too big or small for your monitor, so the next step is to scale it using the `width` and `height` variables you created earlier.

	```python
	difference = pygame.transform.scale(difference, (width, height))
	```
	
1. These lines have just loaded the image into the Raspberry Pi's memory. To display them on the screen, you need to 'blit the image onto the window, and then update the display to show it.

    ``` python
    screen.blit(difference, (0, 0))
    pygame.display.update()
    ```
	
    This line blits the image to the coordinates `x = 0` and `y = 0`; that is, the top-left corner of the image is being placed in the top-left corner of the window.

1. Save and run the file again to see the image displayed.

1. You might find that the image doesn't display for long enough for you to see it, so you can add a small `sleep` to the end of the program, just before Pygame quits.

	```python
	screen.blit(difference, (0,0))
	pygame.display.update()
	
	sleep(3)
	pygame.quit()
	```

## Switching images

1. To switch the image to the scary one, you need to add a pause and then re-blit another image.

1. First, you load the scary image into memory and scale it in the same way you did before with the `difference` image.

	```python
	zombie = pygame.image.load('Scary_Face.png')
	zombie = pygame.transform.scale(zombie, (width, height))
	```
	
1. Then get your program to pause for a few seconds.

	```python
	sleep(3)
	```
	
1. Then you can blit the image to the display, and update the display.

    ``` python
	screen.blit(zombie, (0,0))
	pygame.display.update()
    ```

1. Save and run the program again, to see the new image being placed.

1. It's a little predictable at the moment, so you can add some randomness by changing the `sleep` time between the two images to a random number.

	```python
	sleep(randrange(5,15))
	```
	
## Adding some sound

1. Now it's time to add the scream, to make the game a little scarier. In Python, just like you did with the images, the sound needs to be loaded first. You want to do this **before** the second image is displayed. Change your code so it looks like this:

    ``` python
	zombie = pygame.transform.scale(zombie, (width, height))

	scream = pygame.mixer.Sound("scream.wav")
	
	sleep(randrange(5,15))
    ```

1. Then, you want to start playing the sound just before the second image is shown, as soon as the sleep has finished.

    ``` python
    scream.play()
    ```

1. Next, stop the scream just before Pygame quits:

    ``` python
    scream.stop()
    pygame.quit()
    ```

1. You might find that, depending on your Raspberry Pi model, the scream takes a little time to start playing. You could, therefore, add a little sleep just after the `scream.play()` line.

Your complete code should look like this:

```python	
import pygame
from pygame.locals import*
from time import sleep
from random import randrange

pygame.init()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

screen = pygame.display.set_mode((width, height), FULLSCREEN)

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
	
## Pranking your friends

1. Now all you need to do is have a friend come and try out your Spot the Difference game. Tell them they have a minute to find as many differences as they can, and then watch them jump out of their skins when the scary image appears!

## What next?

- Could you make the game more realistic? Have a look at the [Pygame website](http://www.pygame.org/docs/tut/newbieguide.html) and see if you can learn how to capture mouse clicks from your victim. 
- Could you make the game could keep a fake score of differences spotted before the scary face jumps out?
