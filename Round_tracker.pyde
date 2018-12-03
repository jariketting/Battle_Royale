state = 0 #0 = menu. 1 = running
players = 2
maxplayers = 8
turn = 1
rnd = 1
#radzone
radzone = 0
radsize = 16
radleft = 3
boardsize = 26

#button coordinates
b1x = 48
b1y = 48

b2x = 256
b2y = 48

sbx = 128
sby = 128
sbw = 112

nbx = 64
nby = 320
nbw = 96
nbh = 48

tx = 184

rsize = 64

def draw_radzone(rz):
    global radzone, radsize, boardsize
    for xx in range(26+1):
        for yy in range(26+1):
            if xx == boardsize and yy != boardsize: #vertical coordinates
                fill(0)
                text(chr(yy+65),(xx+0.5)*radsize+200,(yy+0.5)*radsize+200)
            elif yy ==boardsize and xx != boardsize: #horizontal coordinates
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
    #the MOVE THE RADZONE indicator
    if radleft == 2 and rnd > 3 and radzone <= boardsize//2:
        fill(255,63,63)
        text('MOVE THE RADIATION ZONE!',13*radsize+200,-1*radsize+200)

def setup():
    size(750,750)
    textAlign(CENTER,CENTER)

def draw():
    global state, rsize, players, b1x, b1y, b2x, b2y, sbx, sby, sbw, tx, turn, rnd, nbx, nby, nbw, nbh, test
    background(150)
    text(state,5,5)
    if state == 0:
        #minus button
        fill(255)
        rect(b1x,b1y,rsize,rsize)
        fill(0)
        rect(b1x+8,b1y+28,rsize-16,8)
        
        #plus button
        fill(255)
        rect(b2x,b2y,rsize,rsize)
        fill(0)
        rect(b2x+8,b2y+28,48,8)
        rect(b2x+28,b2y+8,8,48)
        
        #playercount
        fill(0)
        text(str(players)+' players',tx,80)
        
        #start button
        fill(255)
        rect(sbx,sby,sbw,rsize)
        fill(0)
        text('start',tx,sby+32)
    if state == 1:
        #player list
        for i in range(players):
            i += 1
            fill(0)
            if turn == i:
                fill(200,255,200)
            text('Player '+str(i),40,40+i*20)
        #current round
        fill(0)
        text('Round '+str(rnd)+' , Radzone: '+str(radzone)+' , Radleft: '+str(radleft),60+100,40)
        #next turn button
        fill(255)
        rect(nbx,nby,nbw,nbh)
        fill(0)
        text('Next turn',nbx+nbw/2,nby+nbh/2)
        #radzone
        draw_radzone(radzone)

def mouseReleased():
    global players, maxplayers, state, turn, rnd, boardsize, radzone, radleft
    if mouseButton == LEFT:
        if state == 0:
            if mouseX >= b1x and mouseX < b1x+rsize and mouseY >= b1y and mouseY < b1y+rsize: #minus button
                if players > 2:
                    players -= 1
                elif players == 2:
                    players = maxplayers
            if mouseX >= b2x and mouseX < b2x+rsize and mouseY >= b2y and mouseY < b2y+rsize: #plus button
                if players < 8:
                    players += 1
                elif players == 8:
                    players = 2
            if mouseX >= sbx and mouseX < sbx+sbw and mouseY >= sby and mouseY < sby+rsize: #start button
                state = 1 #go to the round counter
        if state == 1:
            if mouseX >= nbx and mouseX < nbx+nbw and mouseY >= nby and mouseY < nby+nbh: #next turn button
                turn += 1
                if turn > players: #next round, back to player 1
                    turn = 1
                    rnd += 1
                    #move the radzone
                    if radzone <= boardsize//2:
                        radleft -= 1
                        if radleft == 0:
                            radleft = 2
                            radzone+=1
