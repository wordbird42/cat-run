import numpy as np
from PIL import Image
import random

class Obstacle:
    list = [90, 118, 146, 174, 202]

    def __init__(self, width):
        self.image = Image.open('rock.png')
        self.state = False
        self.width = width
        self.y = random.choice(Obstacle.list)
        self.position = np.array([width, self.y], dtype = int)
        Obstacle.list.remove(self.y)


    def move(self):
        if self.state:
            self.position[0] -= 3
            if self.position[0] < -50:
                Obstacle.list.append(self.y)
                self.y = random.choice(Obstacle.list)
                Obstacle.list.remove(self.y)
                self.position[0] = self.width
                self.position[1] = self.y