import numpy as np
from PIL import Image

class Background:
    def __init__(self, position):
        if position == 0:
            self.image = Image.open('bg3.png')
        elif position == 240:
            self.image = Image.open('bg4.png')
        self.position = np.array([position, 0], dtype = int)
    
    def move(self):
        self.position[0] -= 3
        if self.position[0] == -240:
            self.position[0] = 240