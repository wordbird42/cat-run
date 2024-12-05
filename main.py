from PIL import Image, ImageDraw, ImageFont
import time
from colorsys import hsv_to_rgb
from Cat import Cat
from Obstacle import Obstacle
from Joystick import Joystick
from Background import Background

ROCK = (42, 30)


def collide(cat, obs, draw):
    if cat.status == 'normal':
        if cat.position[2] - 10 >= obs.position[0] and cat.position[0] + 10 <= obs.position[0] + ROCK[0]:
            if cat.position[3] > obs.position[1] + 10 and cat.position[3] < obs.position[1] + 40:
                draw.line([(0, 0), (240, 0)], fill = (255, 0, 0, 255), width = 2)
                draw.line([(0, 239), (240, 239)], fill = (255, 0, 0, 255), width = 2)
                cat.status = 'immune'
                return True

def main():
    joystick = Joystick()
    screen = Image.new("RGBA", (joystick.width, joystick.height))
    draw = ImageDraw.Draw(screen)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)


    car = Image.open('title.png')
    screen.paste(car, (0, 0))
    joystick.disp.image(screen)
    time.sleep(1.5)


    cat = Cat(joystick.width, joystick.height)
    obs1 = Obstacle(joystick.width)
    obs2 = Obstacle(joystick.width)
    obs3 = Obstacle(joystick.width)
    obs4 = Obstacle(joystick.width)
    bg1 = Background(0)
    bg2 = Background(240)
    n = 1


    while True:
        menu = Image.open('menu' + str(n) + '.png')
        screen.paste(menu, (0, 0))
        joystick.disp.image(screen)


        if not joystick.button_U.value:
            n -= 1
        elif not joystick.button_D.value:
            n += 1
        time.sleep(0.13)

        if n <= 0:
            n = 3
        if n >= 4:
            n = 1

        if not joystick.button_A.value or not joystick.button_B.value:

            if n == 3:
                joystick.backlight.value = False
                break

            elif n == 2:
                time.sleep(0.2)
                while joystick.button_A.value and joystick.button_B.value:
                    draw.rectangle((0, 0, joystick.width, joystick.height), fill = (150, 200, 200))
                    draw.text((10, 0), 'Scoreboard', fill = (0, 200, 0), font = font)
                    with open('scores.txt', 'r', encoding = 'utf-8') as file:
                        for i in range(1, 11):
                            draw.text((10, i*22), file.readline(), fill = (0, 0, 0), font = font)
                    joystick.disp.image(screen)


            elif n == 1:

                start = int(time.time())
                heart = 3
                cat.reset(joystick.width, joystick.height)
                obs2.state = False
                obs3.state = False
                obs4.state = False
                obs1.reset()
                obs2.reset()
                obs3.reset()
                obs4.reset()


                while True:

                    command = None
                    if not joystick.button_U.value:
                        command = 'up_pressed'

                    elif not joystick.button_D.value:
                        command = 'down_pressed'
    
                    else:
                        command = None

            
                    obs1.state = True
                    rn = int(time.time())
                    t = rn - start
                    if t == 3:
                        obs2.state = True
                    if t == 5:
                        obs3.state = True
                    if t == 10:
                        obs4.state = True

            

                    cat.move(command)
                    obs1.move()
                    obs2.move()
                    obs3.move()
                    obs4.move()
                    bg1.move()
                    bg2.move()


                    screen.paste(bg1.image, (tuple(bg1.position)))
                    screen.paste(bg2.image, (tuple(bg2.position)))

                    draw.text((4, 2), str(rn - start), fill = (255, 255, 255), font = font)
            
                    screen.paste(obs1.image, (tuple(obs1.position)), mask=obs1.image)
                    screen.paste(obs2.image, (tuple(obs2.position)), mask=obs2.image)
                    screen.paste(obs3.image, (tuple(obs3.position)), mask=obs3.image)
                    screen.paste(obs4.image, (tuple(obs4.position)), mask=obs4.image)
                    screen.paste(cat.image, (tuple(cat.position)), mask=cat.image)
            

                    if collide(cat, obs1, draw):
                        heart -= 1
                    if collide(cat, obs2, draw):
                        heart -= 1
                    if collide(cat, obs3, draw):
                        heart -= 1
                    if collide(cat, obs4, draw):
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

            
                    draw.text((220, 4), str(heart), fill = (255, 150, 150), font = font)

                    joystick.disp.image(screen)

                    if heart == 0:
                        with open('scores.txt', 'r', encoding = 'utf-8') as file:
                            scores = list(file.read().split('\n'))
                            scores.remove('')
                            scores = [int(i) for i in scores]
                            scores.append(t)
                            scores.sort()
                        with open('scores.txt', 'w') as file:
                            for i in scores:
                                file.write(str(i) + '\n')
                        time.sleep(3)
                        break
        




if __name__ == '__main__':
    main()