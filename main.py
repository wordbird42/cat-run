from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Cat import Cat
from Obstacle import Obstacle
from Joystick import Joystick

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)

    cat = Cat(joystick.width, joystick.height)
    obs1 = Obstacle(joystick.width, joystick.height)
    obs2 = Obstacle(joystick.width, joystick.height)

    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))

    while True:
        command = None
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'

        elif not joystick.button_D.value:  # down pressed
            command = 'down_pressed'

        #elif not joystick.button_L.value:  # left pressed
        #    command = 'left_pressed'

        #elif not joystick.button_R.value:  # right pressed
        #    command = 'right_pressed'
            
        else:
            command = None

        cat.move(command)
        obs1.move()
        obs2.move()


        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        my_draw.rectangle((tuple(obs1.position)), fill = (0, 255, 0))
        my_draw.rectangle((tuple(obs2.position)), fill = (0, 255, 0))
        my_draw.ellipse(tuple(cat.position), outline = cat.outline, fill = (0, 0, 0))

        
        
        joystick.disp.image(my_image)



if __name__ == '__main__':
    main()