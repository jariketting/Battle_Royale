import random
import time

roll = 1

timer = 0

# the way it is going to look
def setup():
    global img, img2, img3
    size(400, 400)
    background(0, 0, 0)
    textSize(28)
    text('The number on the dice is...', 10, 50)
    fill(255)
    img = loadImage("Dice_1.png")
    img2 = loadImage("Dice_2.png")
    img3 = loadImage("Dice_3.png")

def Dice_roll():
    Roll = int(random.randint(1, 3))
    return Roll


def draw():
    global roll, timer
    if timer >= 0:
        if timer % 5 == 0:
            roll = Dice_roll()
        timer = timer - 1
    
    if roll==1:
        text('The number on the dice is...', 10, 50)
        image(img, 100, 100, width / 2, height / 2)
    elif roll==2:
        text('The number on the dice is...', 10, 50)
        image(img2, 100, 100, width / 2, height / 2)
    else:
        text('The number on the dice is...', 10, 50)
        image(img3, 100, 100, width / 2, height / 2)
    
def mousePressed():
    global timer
    timer = 200
