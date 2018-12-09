"""
Main file of the application.
"""


# imports
import time

state = 0  # stores state of the game (0 = splash screen, 1 = player screen, 2 =?...)

"""
Setup the application and change any settings according to the designs specs.
"""
def setup():
    size(1366, 768)  # set size of application according to designs specs
    background(19, 19, 19)  # set background color of application
    
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

 
"""
Splash screen (state 0)

This is the screen the user will first be presented with when launching the application.
"""   
def splash_screen():
    bg = loadImage("images/splash_screen.png")
    image(bg, 0, 0)
    
    
"""
Payer screen (state 1)

In this screen the player will add up to 8 players (min = 2) and can start the game
"""    
def player_screen():
    bg = loadImage("images/player_screen.png")
    image(bg, 0, 0)
    
