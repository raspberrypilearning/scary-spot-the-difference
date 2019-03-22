## Getting started

You're going to need two images and a sound file for this activity.

--- task ---
Download and unzip the resources [here](http://rpf.io/p/en/scary-spot-the-difference-go){:target="_blank"}, or alternatively you can download the two images and the sound file below.
--- /task ---

![image](images/spot_the_diff.png)
![image](images/scary_face.png)
<audio>
controls
src="resources/scream.wav3">
Your browser does not support the<code>audio</code> element.
</audio>
[rpf.io/scream](http://rpf.io/scream).

--- task ---
Either open the `scary_spot_the_difference.py` file from the resources, in the editor of your choice ([we recommend using Mu](https://projects.raspberrypi.org/en/projects/getting-started-with-mu), or copy and paste the code below into a new file.

```python
import pygame
from time import sleep
from random import randrange

pygame.init()
```
--- /task ---
