## Get started

You're going to need two images and a sound file for this activity.

--- task ---
Either [download the resources here](http://rpf.io/p/en/scary-spot-the-difference-go){:target="_blank"} and unzip the folder, or download the two images and the sound file below.
--- /task ---

![image](images/spot_the_diff.png)
![image](images/scary_face.png)

<audio controls>
<source src="resources/scream.wav" type="audio/wav">
Your browser does not support the<code>audio</code> element.
</audio>

--- task ---
Either open the `scary_spot_the_difference.py` file (from [the resources](http://rpf.io/p/en/scary-spot-the-difference-go){:target="_blank"}) in your favourite editor application ([for example Mu](https://projects.raspberrypi.org/en/projects/getting-started-with-mu)), or copy and paste the code below into a new file.

```python
import pygame
from time import sleep
from random import randrange

pygame.init()
```
--- /task ---
