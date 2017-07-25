## Switching images

- To switch the image to the scary one, you need to add a pause and then re-blit another image.

- First, you load the scary image into memory and scale it in the same way you did before with the `difference` image.

	```python
	zombie = pygame.image.load('Scary_Face.png')
	zombie = pygame.transform.scale(zombie, (width, height))
	```
	
- Then get your program to pause for a few seconds.

	```python
	sleep(3)
	```
	
- Then you can blit the image to the display, and update the display.

    ``` python
	screen.blit(zombie, (0,0))
	pygame.display.update()
    ```

- Save and run the program again, to see the new image being placed.

- It's a little predictable at the moment, so you can add some randomness by changing the `sleep` time between the two images to a random number.

	```python
	sleep(randrange(5,15))
	```
	
