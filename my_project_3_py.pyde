def setup():
    global x, y, u, t
    size(500,500)
    x, y, u, t = 30, 10, 5, 1
    
def draw():
    global x, y, u, t
    background(255)
    ellipse(x, y, 20, 20)
    if (x == 490 or x == 10) :
        u *= -1
        x += u
    if x != 490:
        x += u
    if y == 490 or y < 0:
        t *= -1
    y += t
    
        
    
