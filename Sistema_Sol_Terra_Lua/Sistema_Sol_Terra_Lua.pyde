#Sol-Terra-Lua
def setup():
    size(800,800)

def desenhaSistemaSolar():
    r = 160
    #Sol
    circle(0,0,70)
    
    pushMatrix()
    rotate(frameCount/(20*TWO_PI))
    #Terra
    circle(r,0,20)
    translate(r,0)
    rotate(frameCount/(5*TWO_PI))   
    #Lua 
    circle(30,0,10)
    popMatrix()
    

def draw():
    background(200)
    translate(width/2,height/2)
    line(-width/2,0,width/2,0)
    line(0,height/2,0,-height/2)
    
    desenhaSistemaSolar()
