from Glow import Glower
import random

def setup():
    global glowers, click_intensity, click_reactivity
    size(800, 600, FX2D)
    # fullScreen(FX2D)
    pixelDensity(displayDensity());
    nb_glowers = 100
    click_intensity = 400
    click_reactivity = 0.50
    glowers = []
    for i in range(nb_glowers):
        glowers.append(Glower())
    
def draw():
    background(0)
    noStroke()
    # print(frameRate)
    for glower in glowers:
        glower.plot()
    
def mouseClicked():
    for glower in glowers:
        if is_near_mouse(glower.x, glower.y):
            glower.x = lerp(glower.x,
                            glower.x+random.uniform(-click_intensity, click_intensity),
                            click_reactivity)
            glower.y = lerp(glower.y,
                            glower.y+random.uniform(-click_intensity, click_intensity),
                            click_reactivity)
        

def is_near_mouse(x, y):
    if (x - mouseX)**2 + (y - mouseY)**2 < 60**2:
        return True
    else:
        return False
    
