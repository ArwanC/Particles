from Glow import Glower
import random

fr = 120

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
        g.update()
        g.plot()
    
    if mousePressed:
        for g in glowers:
            g.attraction = False
            
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
    
    
def mouseReleased():
    for g in glowers:
        g.attraction = True    


def keyPressed():
    global glowers
    if key == ' ':
        glowers.append(Glower())
    elif key == 'R':
        glowers = []
    
