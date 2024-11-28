import numpy as np
from PIL import Image

class Cat:
    def __init__(self, width, height, appearance):
        self.appearance = appearance
        self.image = Image.open(self.appearance)
        self.position = np.array([width/2 - 77, height/2, width/2 - 23, height/2 + 56], dtype = int)
        self.status = 'normal'

    def move(self, command = None):
        if command == 'up_pressed':
            if self.position[1] > 55:
                self.position[1] -= 5
                self.position[3] -= 5

        elif command == 'down_pressed':
            if self.position[3] < 238:
                self.position[3] += 5
                self.position[1] += 5


    def change(self, new):
        self.appearance = new
        self.image = Image.open(self.appearance)