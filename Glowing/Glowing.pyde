from Glow import Glower
import random

fr = 120
max_fr = 120
looping = True
hide_info = False
collision = False

def setup():
    global objects
    size(800, 600, FX2D)
    # fullScreen(FX2D)
    frameRate(fr)
    pixelDensity(displayDensity());
    nb_objects = 1
    objects = []
    for i in range(nb_objects):
        objects.append(Glower(objects))
    
    
def draw():
    global fr
    background(0)
    noStroke()
    
    for o in objects:
        if collision:
            o.collide()
        if looping:
            o.update()
        o.plot()
    
    if mousePressed:
        for o in objects:
            o.attraction = False
            
    if not hide_info:
        textSize(30)
        fill(255, 255, 255, 100)
        text("count "+str(len(objects)), 20, 40)
        
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
    for o in objects:
        o.attraction = True    


def keyPressed():
    global objects, looping, hide_info, max_fr, collision
    if key == ' ':
        objects.append(Glower(objects, collision))
    elif key == 'R':
        objects = []
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
    elif key == 'C':
        collision = not collision
        for object in objects:
            object.collision = not object.collision
        
