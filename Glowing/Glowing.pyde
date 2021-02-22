from Glow import Glower
import random

def setup():
    global glowers
    size(800, 600, FX2D)
    # fullScreen(FX2D)
    pixelDensity(displayDensity());
    nb_glowers = 1
    glowers = []
    for i in range(nb_glowers):
        glowers.append(Glower())
    
def draw():
    # global glowers
    background(0)
    noStroke()
    # print(frameRate)
    for g in glowers:
        g.update()
        g.plot()
    
    if mousePressed:
        for g in glowers:
            g.attraction = False
    
    textSize(30)
    fill(255, 255, 255, 100)
    text("count "+str(len(glowers)), 20, 40)
    if frameRate >= 30:
        fill(0, 255, 0, 100)
    else:
        fill(255, 0, 0, 100)
    text("fps "+str(int(frameRate)), 20, 80)
    
        
# def mouseClicked():
#     glowers.append(Glower())
    
def mouseReleased():
    for g in glowers:
        g.attraction = True    

def keyPressed():
    global glowers
    if key == ' ':
        glowers.append(Glower())
    elif key == 'R':
        glowers = []
    
