"""
Main file of the application.
"""

# imports
import time
from Controller import Controller

state = 0  # stores state of the game (0 = splash screen, 1 = player screen, 2 =?...)
image_dir = "images/"  # directory images are stored in
controller = Controller()

# stores all buttons withing app
buttons = [
    [0, 0, 0, 0],  # start button
    [0, 0, 0, 0],  # add player button
    [0, 0, 0, 0]  # remove player button
]

"""
Setup the application and change any settings according to the designs specs.
"""
def setup():
    size(1366, 768)  # set size of application according to designs specs
    background(19)  # set background color of application
    frameRate(60)  # set framerate
    
    # add one player on default
    controller.add_player('Player 1')
    
    # start application with splash screen
    splash_screen()
    

"""
This function will keep looping until the application has been terminated.

The main functionality is to call the correct function based on the state of the game, together with some other small stuff (like the timer showing the splash screen for 3 secs)
"""
def draw():
    # global variables
    global state
    
    # check what state the game is in
    if state == 0:
        # splash screen has to be displayer for 3 seconds, then the next screen will be shown by chaching the state
        
        time.sleep(3)  # wait 3 seconds
        state = 1  # change state of game to 1
        clear()  # screen has to be cleared, otherwise the old screen will still be visible trought the new one
    elif state == 1:
        # player screen
        player_screen()
    elif state == 2:
        #main screen
        main_screen()
    
        
"""
When the player clicks on the screen, this function will check if a button was clicked.

Buttons are stored in the buttons var. And are pointed to by it's index key
"""
def mouseReleased():
    # get required global vars
    global buttons, state, controller
    
    # go trough each button and check if it is pressed
    for button, cords in enumerate(buttons):
        # check if players clicked location falls withing the buttons cords
        if mouseX >= cords[0] and mouseX <= cords[2] and mouseY >= cords[1] and mouseY <= cords[3]:
            # some buttons can only be pressed in specific stages of the application, check what state the game is in
            if state == 1:
                # check if button is button 0
                if button == 0:
                    # check if min players count is met
                    if len(controller.get_players()) >= 2:
                        state = 2  # change state to two to start the game
                        clear()  # clear current screen
                # check if button is button 1
                elif button == 1:
                    # only allow the button to be pressed when the player count is lower than eight
                    if len(controller.get_players()) < 8:
                        controller.add_player("Player " + str(len(controller.get_players()) + 1))
                # check if button is button 2
                elif button == 2:
                    if len(controller.get_players()) > 1:
                        controller.remove_player(-1)
                        clear()

 
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
        rect(xpos, ypos, 55, 53)  # create rect with players color
        
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
    global controller
    
    # draw main screen image
    bg = loadImage(image_dir+"main_screen.png")
    image(bg, 0, 0)
    
    # create font for turn
    font = createFont("Arial Bold", 50, True)
    textFont(font)
    fill(0)
    textAlign(CENTER)
    
    text(controller.get_round(), 1210, 220) 
    
