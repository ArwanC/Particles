import random

class Glower():
    def __init__(self):
         
        self.radius = 50
        self.x = mouseX
        self.y = mouseY
        self.reactivity = random.uniform(0.0001, 0.001)
        self.c1 = color(255, 255, 255)
        self.c2 = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def update(self):
        self.x = lerp(self.x, mouseX, self.reactivity)
        self.y = lerp(self.y, mouseY, self.reactivity)
        
    def plot(self):
        for r in range(self.radius, 0, -1):
            h = map(r, 0, self.radius, 0, 0.3)
            c = lerpColor(self.c1, self.c2, h)
            a = int(map(r, self.radius, 0, 0, 255/10))
            fill(c, a)
            self.update()
            ellipse(self.x, self.y, r, r)
