class winscreen(object): 
    def __init__ (self):
        self.x = 0
        self.y = 0

    
    def show(self): 
       background(0) 
       textSize(62)
       fill(255,255,255)
       text("Winner Winner!",683-self.x - 200 ,384-self.y) 
       img = loadImage("design.png")
       image(img, 683-self.y-100,50, width / 6, height / 4)
       textSize(42)
       text(".. has won the game!",683-self.x-100 ,384-self.y + 100) 

def setup():
    size(1366,768)
    global win
    win = winscreen()
def draw():
    win.show()
