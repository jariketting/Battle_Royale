class HP(object): 
    def __init__ (self):
        self.x = 100
        self.y = 100 
        global radius
        radius = 7
    
    def show(self): 
        fill(0)
        rect(self.x,self.y,250,40,radius)
        rect(self.x,self.y+60,250,40,radius)
        textSize(32)
        fill(255,255,255)
        text("Health", self.x+10, self.y+30)
        fill(255,255,255)
        text("Armor", self.x+10, self.y+90)
        text("10",self.x+200, self.y+30)
        text("0",self.x+200, self.y+90)
        
def setup():
    size(600,600)
    global hp
    hp = HP()
def draw():
    hp.show()
