def setup():
    size(800,600)

def draw():
    background(128)
    p2x = 100
    p2y = 100
    p1x = 100
    p1y = 300
    p3x = mouseX #700
    p3y = mouseY #300
    p4x = 700
    p4y = 300
    beginShape()
    vertex(p1x,p1y)
    t = 0
    while t <= 1:
        ax = p1x + t*(p2x-p1x)
        bx = p2x + t*(p3x-p2x)
        cx = p3x + t*(p4x-p3x)
        dx = ax + t*(bx-ax)
        ex = bx + t*(cx-bx)
        fx = dx + t*(ex-dx)
        ay = p1y + t*(p2y-p1y)
        by = p2y + t*(p3y-p2y)
        cy = p3y + t*(p4y-p3y)
        dy = ay + t*(by-ay)
        ey = by + t*(cy-by)
        fy = dy + t*(ey-dy)
        vertex(fx,fy)
        # vertex(p3x,p3y)        
        t = t + 0.01
        
    vertex(p4x,p4y)
    endShape()
    
