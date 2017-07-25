## Setting up your file

- Open IDLE by clicking on Menu> Programming > Python 3 (IDLE), then click File and New File.

- Save your file straight away, in the same directory as your images. If you call it `run_me.py`, you won't be giving the game away to your victim.

- To begin with, you'll need to import the Pygame library and some of its modules. You're also going to need the `sleep` and `randrange` functions.

    ``` python
    import pygame
    from pygame.locals import*
	from time import sleep
	from random import randrange
    ```
	
- Next, you need to initialise Pygame so that it's ready to be used. As different monitors have different sizes, you need to find out the width and height of your monitor, and save them as variables.

    ``` python
	pygame.init()

	width = pygame.display.Info().current_w
	height = pygame.display.Info().current_h
	```
    
- Lastly for this section, you can instruct Pygame to create a full-screen window for the game to be played in, and then get Pygame to quit.

    ``` python
	screen = pygame.display.set_mode((width, height), FULLSCREEN)
	
	pygame.quit()
    ```

- Save your file again and then run it by pressing `F5`.

- You should see a blank rectangular window open. This is the Pygame window. It should close itself straight away, as your program reaches the `pygame.quit()` line.

