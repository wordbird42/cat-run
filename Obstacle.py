import numpy as np
import random

class Obstacle:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        self.start = width
        self.height = height
        self.loc = random.randrange(0, height)
        self.position = np.array([width-20, self.loc, width, self.loc + 20])
        self.outline = "#FFFFFF"

    def move(self, command = None):
        self.position[0] -= 3
        self.position[2] -= 3

        if self.position[0] < -20:
            self.loc = random.randrange(0, self.height)
            self.position = [self.start-20, self.loc, self.start, self.loc + 20]