from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Cat import Cat
from Obstacle import Obstacle
from Joystick import Joystick

def main():
    joystick = Joystick()
    screen = Image.new("RGBA", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(screen)

    joystick.disp.image(screen)

    with open('user.txt', 'r', encoding = 'utf-8') as car:
        car = car.readline()[:-1]

    cat = Cat(joystick.width, joystick.height, car)
    obs1 = Obstacle(joystick.width, joystick.height)
    obs2 = Obstacle(joystick.width, joystick.height)

    #put title display

    while True:
        #show menu
        if not joystick.button_A.value:
                break

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


            draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
            draw.rectangle((tuple(obs1.position)), fill = (0, 255, 0))

        
            screen.paste(cat.image, (tuple(cat.position)), mask=cat.image)

        
        
            joystick.disp.image(screen)
        
            if not joystick.button_A.value:
                break



if __name__ == '__main__':
    main()