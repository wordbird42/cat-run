from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Cat import Cat
from Obstacle import Obstacle
from Joystick import Joystick
from Background import Background

ROCK = (42, 30)

def front(cat, obs, screen):
    if cat.position[3] >= obs.position[1] + ROCK[1]:
        screen.paste(obs.image, (tuple(obs.position)), mask=obs.image)
        screen.paste(cat.image, (tuple(cat.position)), mask=cat.image)
    else: 
        screen.paste(cat.image, (tuple(cat.position)), mask=cat.image)
        screen.paste(obs.image, (tuple(obs.position)), mask=obs.image)

def collide(cat, obs, draw):
    if cat.status == 'normal':
        if cat.position[2] - 10 >= obs.position[0] and cat.position[0] + 10 <= obs.position[0] + ROCK[0]:
            if cat.position[3] > obs.position[1] + 10 and cat.position[3] < obs.position[1] + 42:
                draw.line([(0, 0), (240, 0)], fill = (255, 0, 0, 255), width = 2)
                draw.line([(0, 239), (240, 239)], fill = (255, 0, 0, 255), width = 2)
                cat.status = 'immune'
                return True

def main():
    joystick = Joystick()
    screen = Image.new("RGBA", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(screen)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)

    joystick.disp.image(screen)

    with open('user.txt', 'r', encoding = 'utf-8') as car:
        car = car.readline()[:-1]

    cat = Cat(joystick.width, joystick.height, car)
    obs1 = Obstacle(joystick.width)
    obs2 = Obstacle(joystick.width)
    obs3 = Obstacle(joystick.width)
    bg1 = Background(0)
    bg2 = Background(240)

    #put title

    while True:
        #show menu
        if not joystick.button_A.value:
                break

        start = int(time.time())
        heart = 3

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

            
            obs1.state = True
            rn = int(time.time())
            if rn - start == 3:
                obs2.state = True
            if rn - start == 6:
                obs3.state = True

            

            cat.move(command)
            obs1.move()
            obs2.move()
            obs3.move()
            bg1.move()
            bg2.move()


            screen.paste(bg1.image, (tuple(bg1.position)))
            screen.paste(bg2.image, (tuple(bg2.position)))

            draw.text((4, 2), str(rn - start), fill = (255, 255, 255), font = font)
            
            screen.paste(obs1.image, (tuple(obs1.position)), mask=obs1.image)
            screen.paste(obs2.image, (tuple(obs2.position)), mask=obs2.image)
            screen.paste(obs3.image, (tuple(obs3.position)), mask=obs3.image)
            screen.paste(cat.image, (tuple(cat.position)), mask=cat.image)
            

            if collide(cat, obs1, draw):
                heart -= 1
            if collide(cat, obs2, draw):
                heart -= 1
            if collide(cat, obs3, draw):
                heart -= 1

            

            if cat.status == 'immune':
                timer = rn
                cat.status = 'timer'
            
            if cat.status == 'timer':
                if rn - timer < 1:
                    draw.line([(0, 0), (240, 0)], fill = (255, 0, 0, 255), width = 2)
                    draw.line([(0, 239), (240, 239)], fill = (255, 0, 0, 255), width = 2)
                elif rn - timer < 3:
                    draw.line([(0, 0), (240, 0)], fill = (255, 255, 255, 255), width = 2)
                    draw.line([(0, 239), (240, 239)], fill = (255, 255, 255, 255), width = 2)
                if rn - timer == 3:
                    cat.status = 'normal'

            
            draw.text((220, 4), str(heart), fill = (255, 255, 255), font = font)

            joystick.disp.image(screen)


        
            if not joystick.button_A.value:
                break



if __name__ == '__main__':
    main()