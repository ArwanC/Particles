from Glow import Glower
import random

fr = 120
max_fr = 120
looping = True
hide_info = False
collision = False
speed_limit = False
record = False

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
        alfa = 100
        # Object count
        fill(255, 255, 255, alfa)
        text("count: "+str(len(objects)), 20, 40)
        
        # FPS
        if frameCount%60 == 1:
            fr = frameRate
        if fr >= 30:
            fill(0, 255, 0, alfa)
        else:
            fill(255, 0, 0, alfa)
        text("fps: "+str(int(fr)), 20, 80)
        
        # Collision
        if not collision:
            fill(255, 0, 0, alfa)
        else:
            fill(0, 255, 0, alfa)
        text("collision: "+str(collision), 160, 40)
        
        # Speed
        if speed_limit:
            fill(255, 0, 0, alfa)
        else:
            fill(0, 255, 0, alfa)
        text("speed: "+("Slowed" if speed_limit else "Max"), 160, 80)
        
    
    noStroke()
    fill(255)
    if mousePressed:
        fill(255, 0, 0)
    ellipse(mouseX, mouseY, 8, 8)
    
    if record:
        saveFrame("frames/particles-######.png")
        fill(255, 0, 0)
        ellipse(width-20, 20, 20, 20)
    
def mouseReleased():
    for o in objects:
        o.attraction = True    


# def keyPressed():
#     global objects, looping, hide_info, max_fr, collision, speed_limit, record
#     if key == ' ':
#         objects.append(Glower(objects, collision))
#     elif key == ('R' or 'r'):
#         objects = []
#     elif key == ('F' or 'f'):
#         looping = not looping
#     elif key == ('H' or 'h'):
#         hide_info = not hide_info
#     elif key == ('S' or 's'):
#         speed_limit = not speed_limit
#         if max_fr == 30:
#             max_fr = 120
#         else:
#             max_fr = 30
#         frameRate(max_fr)
#     elif key == ('C' or 'c'):
#         collision = not collision
#         for object in objects:
#             object.collision = not object.collision
#     elif key == '\n':
#         record = not record
        
