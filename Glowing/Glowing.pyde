from Glow import Glower
import random

fr = 120
max_fr = 120
looping = True
hide_info = False

def setup():
    global glowers
    size(800, 600, FX2D)
    # fullScreen(FX2D)
    frameRate(fr)
    pixelDensity(displayDensity());
    nb_glowers = 1
    glowers = []
    for i in range(nb_glowers):
        glowers.append(Glower())
    
    
def draw():
    global fr
    background(0)
    noStroke()
    
    for g in glowers:
        if looping:
            g.update()
        g.plot()
    
    if mousePressed:
        for g in glowers:
            g.attraction = False
            
    if not hide_info:
        textSize(30)
        fill(255, 255, 255, 100)
        text("count "+str(len(glowers)), 20, 40)
        
        if frameCount%60 == 1:
            fr = frameRate
        if fr >= 30:
            fill(0, 255, 0, 100)
        else:
            fill(255, 0, 0, 100)
        text("fps "+str(int(fr)), 20, 80)
    
    noStroke()
    fill(255)
    if mousePressed:
        fill(255, 0, 0)
    ellipse(mouseX, mouseY, 8, 8)
    
    
def mouseReleased():
    for g in glowers:
        g.attraction = True    


def keyPressed():
    global glowers, looping, hide_info, max_fr
    if key == ' ':
        glowers.append(Glower())
    elif key == 'R':
        glowers = []
    elif key == 'F':
        looping = not looping
    elif key == 'H':
        hide_info = not hide_info
    elif key == 'S':
        if max_fr == 30:
            max_fr = 120
        else:
            max_fr = 30
        frameRate(max_fr)
        
