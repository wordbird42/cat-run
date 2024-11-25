import numpy as np
from PIL import Image

class Cat:
    def __init__(self, width, height, appearance):
        self.appearance = appearance
        self.image = Image.open(self.appearance)
        self.position = np.array([width/2 - 27, height/2 - 28], dtype = int)

    def move(self, command = None):
        if command == 'up_pressed':
            if self.position[1] > 5:
                self.position[1] -= 5

        elif command == 'down_pressed':
            if self.position[1] < 180:
                self.position[1] += 5

        elif command == 'left_pressed':
            self.position[0] -= 5
                
        elif command == 'right_pressed':
            self.position[0] += 5

    def change(self, new):
        self.appearance = new
        self.image = Image.open(self.appearance)