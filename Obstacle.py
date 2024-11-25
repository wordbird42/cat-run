import numpy as np
from PIL import Image
import random

class Obstacle:
    def __init__(self, width, height, appearance):
        self.appearance = appearance
        self.image = Image.open(self.appearance)
        self.state = None
        self.width = width
        self.height = height
        self.position = np.array([width-20, random.randrange(0, height)], dtype = int)

    def move(self):
        self.position[0] -= 3
        self.position[2] -= 3

        if self.position[0] < -20:
            self.position = [self.width-20, random.randrange(0, self.height)]