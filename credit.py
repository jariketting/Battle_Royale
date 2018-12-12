
y_offset = 0

def setup():
    size(1366,768)
    background(0,0,0)
    textAlign(CENTER)
    fill(255,255,255)
    
def draw():
    clear()
    global y_offset
    textSize(150)
    text('Made by',683, 1000+ y_offset)
    textSize(70)
    text('Dani de Jong', 683, 1100 + y_offset)
    text('Jari Ketting', 683, 1200 + y_offset)
    text('Ronan van Kessel', 683, 1300 + y_offset)
    text('Daphne Miedema', 683, 1400 + y_offset)
    y_offset = y_offset - 1
