"""
Main file of the application.
"""

# imports
import time
import random
from Controller import Controller

state = 0  # stores state of the game (0 = splash screen, 1 = player screen, 2 =?...)
image_dir = "images/"  # directory images are stored in
controller = Controller()

roll = 1 
timer = 0
y_offset = 0

# stores all buttons withing app
buttons = [
    [0, 0, 0, 0],  # start button
    [0, 0, 0, 0],  # add player button
    [0, 0, 0, 0],  # remove player button
    [0, 0, 0, 0],  # dice
    [0, 0, 0, 0],  # round tracker hover
    [0, 0, 0, 0]  # next turn
]

dices = []

"""
Setup the application and change any settings according to the designs specs.
"""
def setup():    
    global dices
    
    size(1366, 768)  # set size of application according to designs specs
    background(19)  # set background color of application
    frameRate(60)  # set framerate
    
    # add one player on default
    controller.add_player('Player 1')
    
    # setup dices
    dices = [loadImage(image_dir+"dice_1.png"), loadImage(image_dir+"dice_2.png"), loadImage(image_dir+"dice_3.png")]
    
    # start application with splash screen
    if state == 0:
        splash_screen()
    

"""
This function will keep looping until the application has been terminated.

The main functionality is to call the correct function based on the state of the game, together with some other small stuff (like the timer showing the splash screen for 3 secs)
"""
def draw():
    # global variables
    global state
    
    clear()
    noStroke()  # remove stroke
    background(19)  # set background color of application
    
    # check what state the game is in
    if state == 0:
        # splash screen has to be displayer for 3 seconds, then the next screen will be shown by chaching the state
        
        time.sleep(3)  # wait 3 seconds
        state = 1  # change state of game to 1
    elif state == 1:
        # player screen
        player_screen()
    elif state == 2:
        #main screen
        main_screen()
    elif state == 3:
        return
    elif state == 4:
        credit_screen()
    
        
"""
When the player clicks on the screen, this function will check if a button was clicked.

Buttons are stored in the buttons var. And are pointed to by it's index key
"""
def mouseReleased():
    # get required global vars
    global buttons, state, controller, timer
    
    # go trough each button and check if it is pressed
    for button, cords in enumerate(buttons):
        # check if players clicked location falls withing the buttons cords
        if mouseX >= cords[0] and mouseX <= cords[2] and mouseY >= cords[1] and mouseY <= cords[3]:
            # some buttons can only be pressed in specific stages of the application, check what state the game is in
            if state == 1:
                if button == 0:
                    # check if min players count is met
                    if len(controller.get_players()) >= 2:
                        state = 2  # change state to two to start the game
                elif button == 1:
                    # only allow the button to be pressed when the player count is lower than eight
                    if len(controller.get_players()) < 8:
                        controller.add_player("Player " + str(len(controller.get_players()) + 1))
                elif button == 2:
                    if len(controller.get_players()) > 1:
                        controller.remove_player(-1)
            elif state == 2:
                if button == 3:
                    timer = 50
                elif button == 5:
                    controller.next_turn()

 
"""
Splash screen (state 0)

This is the screen the user will first be presented with when launching the application.
"""
def splash_screen():    
    # draw splash screen image
    bg = loadImage(image_dir+"splash_screen.png")
    image(bg, 0, 0)
    
    
"""
Payer screen (state 1)

In this screen the player will add up to 8 players (min = 2) and can start the game
"""    
def player_screen():
    # get required global vars
    global buttons
    
    # set background
    bg = loadImage(image_dir+"player_screen.png")
    image(bg, 0, 0)
    
    # create start button
    start_button = loadImage(image_dir+"start_button.png")
    buttons[0] = [1112, 683, 1349, 751]  # set cords for start button
    image(start_button, buttons[0][0], buttons[0][1])

    # create font for player names
    player_font = createFont("Arial Bold", 28, True)
    textFont(player_font)
    
    player_image = loadImage(image_dir+"player_name.png")

    # starting cords for the player list
    ypos = 100
    xpos = 429

    # display each player on screen
    for player in controller.get_players():
        image(player_image, xpos, ypos)
        
        fill(200)  # set color of name displayed
        text(player.get_name(), xpos + 67, ypos + 37)  # display players name
        
        fill(*player.get_color())  # fill with players color
        rect(xpos, ypos, 56, 53)  # create rect with players color
        
        ypos += 74  # add to ypos, 54 is size of image + 20 for the margin at the botton of each player
    
    # show add player button when player count is under 8
    if len(controller.get_players()) < 8:
        buttons[1] = [xpos, ypos, xpos + 212, ypos + 45]
        add_player_image = loadImage(image_dir+"add_player_button.png")
        image(add_player_image, xpos, ypos)
    else:
        buttons[1] = [0,0,0,0] # make sure button can not be pressed
        
    # show remove player button when player count is under 8
    if len(controller.get_players()) > 1:
        buttons[2] = [742, ypos, 742 + 212, ypos + 45]
        add_player_image = loadImage(image_dir+"remove_player_button.png")
        image(add_player_image, 742, ypos)
    else:
        buttons[2] = [0,0,0,0] # make sure button can not be pressed


def main_screen():
    global controller, dices, roll, timer

    player = controller.get_current_player()
    players = controller.get_players()

    # draw dice    
    if timer >= 0:
        if timer % 5 == 0:
            roll = dice_roll()
        timer = timer - 1
        
    buttons[3] = [1142, 483, 1283, 624]
    image(dices[roll-1], 1142, 483, 141, 141)
    
    # draw main screen image
    bg = loadImage(image_dir+"main_screen.png")
    image(bg, 0, 0)
    
    # display turn
    font = createFont("Arial Bold", 50, True)
    textFont(font)
    fill(0)
    textAlign(CENTER)
    
    text(controller.get_round(), 1210, 215) 
    
    # display current player
    fill(*player.get_color())  # fill with players color
    rect(210, 36, 63, 63)  # create rect with players color
    
    # create font for player name
    player_font = createFont("Arial Bold", 40, True)
    textFont(player_font)
    
    fill(0)  # set color of name displayed
    textAlign(LEFT)
    text(player.get_name(), 283, 80)  # display players name
    
    # display all players
    reversed_players = players[:]
    reversed_players.reverse()
    
    player_font = createFont("Arial Bold", 28, True)
    textFont(player_font)
    
    player_image = loadImage(image_dir+"player_name_main.png")
    player_image_selected = loadImage(image_dir+"player_name_main_selected.png")

    # starting cords for the player list
    ypos = 695
    xpos = 22

    # display each player on screen
    for player in reversed_players:
        if player == controller.get_current_player():
            image(player_image_selected, xpos-5, ypos-5)
        else:
            image(player_image, xpos, ypos)
        
        fill(0)  # set color of name displayed
        
        if player.is_dead():
            fill(222)  # set color of name displayed
            
        text(player.get_name(), xpos + 55, ypos + 33)  # display players name
        
        fill(*player.get_color())  # fill with players color
        rect(xpos, ypos, 45, 45)  # create rect with players color
        
        ypos -= 51  # add to ypos, 54 is size of image + 20 for the margin at the botton of each player
        
    
    # display players health and armor
    font = createFont("Arial Bold", 40, True)
    textFont(font)
    fill(255)
    textAlign(RIGHT)
    
    text(controller.get_current_player().get_hp(), 820, 185) 
    text(controller.get_current_player().get_armor(), 820, 270) 
    
    # next turn button
    start_button = loadImage(image_dir+"next_turn.png")
    buttons[5] = [1095, 695, 1334, 739]  # set cords for start button
    image(start_button, buttons[5][0], buttons[5][1])
    
    # radiation zone
    font = createFont("Arial Bold", 50, True)
    textFont(font)
    textAlign(CENTER)
    
    if controller.get_radiation_zone():
        fill(191, 0, 0)
        text('YES', 1210, 365) 
    else:
        fill(0)
        text('NO', 1210, 365) 
    
    buttons[4] = [1136, 267, 1288, 400]
    
    if mouseX >= buttons[4][0] and mouseX <= buttons[4][2] and mouseY >= buttons[4][1] and mouseY <= buttons[4][3]:
        draw_radzone()
    

def credit_screen():
    global y_offset

    textAlign(CENTER)
    fill(255)
    textSize(150)
    text('Made by', 683, 1000 + y_offset)
    textSize(70)
    text('Dani de Jong', 683, 1100 + y_offset)
    text('Jari Ketting', 683, 1200 + y_offset)
    text('Ronan van Kessel', 683, 1300 + y_offset)
    text('Daphne Miedema', 683, 1400 + y_offset)
    y_offset = y_offset - 1
    
    if y_offset < -1500:
        y_offset = 0

    
def dice_roll():
    return int(random.randint(1, 3))
    
    
def draw_radzone():
    global controller
    
    radsize = 16
    boardsize = 26
    
    radzone = controller.get_radzone()
    
    # the 'window' behind the board
    textAlign(CENTER,CENTER)
    font = createFont("Arial", 12, True)
    textFont(font)
    fill(127)
    stroke(0);
    rect(180, 180, 40 + (boardsize+1) * radsize, 40 + (boardsize + 1) * radsize)
    
    # the board loop
    for xx in range(boardsize+1):
        for yy in range(boardsize+1):
            if xx == boardsize and yy != boardsize: #vertical coordinates
                fill(0)
                text(chr(yy+65),(xx+0.5)*radsize+200,(yy+0.5)*radsize+200)
            elif yy == boardsize and xx != boardsize: #horizontal coordinates
                fill(0)
                text(str(xx+1),(xx+0.5)*radsize+200,(yy+0.5)*radsize+200)
            elif xx != boardsize and yy != boardsize: #the tiles
                fill(127,127,255)
                rect(xx*radsize+200,yy*radsize+200,radsize,radsize)
                if (xx >= radzone-1 and xx <= boardsize-radzone) and (yy >= radzone-1 and yy <= boardsize-radzone):
                    fill(127,255,127)
                    rect(xx*radsize+200,yy*radsize+200,radsize,radsize)
                if (xx == radzone-1 or xx == boardsize-radzone) or (yy == radzone-1 or yy == boardsize-radzone):
                    fill(255,255,127)
                    rect(xx*radsize+200,yy*radsize+200,radsize,radsize)
                    
    textAlign(LEFT, TOP)
    noStroke()
    
