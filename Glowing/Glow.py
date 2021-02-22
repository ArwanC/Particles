import random
import math

class Glower():
    def __init__(self, others, col=False):
        self.location = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.velocity_limit = random.uniform(7, 10)
        self.mouse_mag = random.uniform(0.3, 1) 
        self.attraction = True
        self.collision = col
        self.others = others
        self.spring = 0.1
        
        self.radius = 50
        self.c1 = color(255, 255, 255)
        self.c2 = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def collide(self):
        for other in self.others:
            if (other.location.x - self.location.x)**2 + (other.location.y - self.location.y)**2 <= (self.radius-20)**2:
                dx = other.location.x - self.location.x
                dy = other.location.y - self.location.y
                angle = math.atan2(dy, dx)
                touching_dist = other.radius + self.radius
                targetX = self.location.x + math.cos(angle)*touching_dist
                targetY = self.location.y + math.sin(angle)*touching_dist
                
                av = PVector(targetX, targetY)
                av.sub(self.location)
                av.mult(self.spring)
                self.velocity.sub(av)
                av = PVector(targetX, targetY)
                av.sub(other.location)
                av.mult(other.spring)
                other.velocity.add(av)

    def update(self):
        if self.attraction:
            mouse = PVector(mouseX, mouseY)
            mouse.sub(self.location)
            mouse.setMag(self.mouse_mag)
            self.acceleration = mouse
        
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.velocity.limit(self.velocity_limit)

    def plot(self):
        # Fading and gradient colored:
        # for r in range(self.radius, 0, -1):
            # h = map(r, 0, self.radius, 0, 0.3)
            # c = lerpColor(self.c1, self.c2, h)
            # a = int(map(r, self.radius, 0, 0, 255/10))
            # fill(c, a)
            # ellipse(self.location.x, self.location.y, r, r)
        stroke(255)
        fill(self.c2, 80)
        if self.collision:
            fill(self.c2)
        ellipse(self.location.x, self.location.y, self.radius-20, self.radius-20)
        
