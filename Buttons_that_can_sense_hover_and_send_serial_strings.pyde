add_library('serial')

noOfLeds = 6                                   
rad = 50
colour = color(254, 14, 14)
highlight = color(219, 80, 80)
press = color(240, 208, 208)                      
X  = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
Y = 150
boolCirc = False

uno = Serial(this, "COM7", 9600)

def overCircle(x, y, radius):
    disX = float(x) - mouseX;
    disY = float(y) - mouseY;
    if sqrt(sq(disX) + sq(disY)) < radius:
        return True
    else:
        return False            
    
            
def setup():
    
    canvas = 400 + (noOfLeds-1)*100
    size(canvas, 2*Y)
    for i in range(noOfLeds):
        ellipse(200+i*100, Y, rad, rad)        
        


def draw():
    for i in range(noOfLeds):
        if overCircle(X[i], Y, rad):
            fill(highlight)
        else:
            fill(colour)
        noStroke()
        ellipse(X[i], Y, rad, rad)
        
def mousePressed():
    for i in range(noOfLeds):
        if overCircle(X[i], Y, rad):
            uno.write(i+1)
            fill(press)
            ellipse(X[i], Y, rad, rad)
            
def mouseReleased():
    for i in range(noOfLeds):
        if overCircle(X[i], Y, rad):
            uno.write(i+1)
            
            
#Known bugs: Clicking in one circle and releasing in another lights up both LEDs.
 
