import numpy as np
from PIL import Image

class Cat:
    def __init__(self, width, height):
        self.appearance = 2
        self.image = Image.open('cat' + str(self.appearance) + '.png')
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

        self.appearance += 1
        if self.appearance == 6:
            self.appearance = 2
        self.image = Image.open('cat' + str(self.appearance//2) + '.png')

    def reset(self, width, height):
        self.position = np.array([width/2 - 77, height/2, width/2 - 23, height/2 + 56], dtype = int)
        self.status = 'normal'
