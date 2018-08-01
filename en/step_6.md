## Displaying an image

- To display an image in Pygame, you first need to load the image. You can start with the Spot the Difference image. Place this line above the `pygame.quit()` line. If you've used a different image, don't forget to change the name.

	``` python
	difference = pygame.image.load('spot_the_diff.png')
	```

- The image may be too big or small for your monitor, so the next step is to scale it using the `width` and `height` variables you created earlier.

	```python
	difference = pygame.transform.scale(difference, (width, height))
	```
	
- These lines have just loaded the image into the Raspberry Pi's memory. To display them on the screen, you need to `blit` the image onto the window, and then update the display to show it.

    ``` python
    screen.blit(difference, (0, 0))
    pygame.display.update()
    ```
	
    This line blits the image to the coordinates `x = 0` and `y = 0`; that is, the top-left corner of the image is being placed in the top-left corner of the window.

- Save and run the file again to see the image displayed.

- You might find that the image doesn't display for long enough for you to see it, so you can add a small `sleep` to the end of the program, just before Pygame quits.

	```python
	screen.blit(difference, (0,0))
	pygame.display.update()
	
	sleep(3)
	pygame.quit()
	```

