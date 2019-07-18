
def setup():
    global x, y, x_s, y_s, a, b, c, d, e, mode, count
    global hit1, hit2, hit3, hit4, hit5, game
    size(550,550)
    x, y, x_s, y_s = 275, 470, -5, -3 #Respectively Xposition, Yposition, Xspeed, Yspeed
    a, b, c, d, e = 255, 255, 255, 255, 255 #Brick Colors
    mode, count = True, 0
    hit1, hit2, hit3, hit4, hit5 = True, True, True, True, True
    game = False
    textSize(32)
    
    
def draw():
    global x, y, x_s, y_s, a, b, c, d, e, mode, count, game
    global hit1, hit2, hit3, hit4, hit5
    if mode == True:
        if game == True:
            background(0)
            stroke(random(120), random(14), random(181))
            fill(a)
            rect(0, 4, 100, 20) #Positioning Brick1
            fill(b)
            rect(110, 4, 100, 20) #Positioning Brick2
            fill(c)
            rect(220, 4, 100, 20) #Positioning Brick3
            fill(d)
            rect(330, 4, 100, 20) #Positioning Brick4
            fill(e)
            rect(440, 4, 100, 20) #Positioning Brick5
        
        
            stroke(15)
            fill(255)
            ellipse(x, y, 20, 20) #Ball
            if y >= 500: # Setting game_over
                mode = False
            if (x >= 500 or x <= 0):
                x_s *= -1
            if (y >= 500 or y <= 0):
                y_s *= -1
            
            x += x_s #Increasing X position
            y += y_s #Increasing Y position
            fill(255)
            rect(mouseX - 40 , 480, 80, 20)
            if (mouseX >= (x - 40) and mouseX <= (x + 40)) and (y >= 480): #Bouncing Balll
                y_s *= -1
                count += 1
                if (mouseX >= (x-40) and mouseX <= x):
                    x_s = 5
                else: x_s = -5
            if (x >= 0 and x <= 100) and (y >= 4 and y <= 24) and hit1: #Brick1
                a, hit1 = 0, False
                y_s *= -1
            if (x >= 110 and x <= 210) and (y >= 4 and y <= 24) and hit2: #Brick2
                b, hit2 = 0, False
                y_s *= -1
            if (x >= 220 and x <= 320) and (y >= 4 and y <= 24) and hit3: #Brick3
                c, hit3 = 0, False
                y_s *= -1
            if (x >= 330 and x <= 430) and (y >= 4 and y <= 24) and hit4: #Brick4
                d, hit4 = 0, False
                y_s *= -1
            if (x >= 440 and x <= 540) and (y >= 4 and y <= 24) and hit5: #Brick5
                e ,hit5 = 0, False
                y_s *= -1
        
        else:
            background(0)
            stroke(random(120), random(14), random(181))
            fill(a)
            rect(0, 4, 100, 20) #Positioning Brick1
            fill(b)
            rect(110, 4, 100, 20) #Positioning Brick2
            fill(c)
            rect(220, 4, 100, 20) #Positioning Brick3
            fill(d)
            rect(330, 4, 100, 20) #Positioning Brick4
            fill(e)
            rect(440, 4, 100, 20) #Positioning Brick5
            
            fill(255)
            rect(235, 480, 80, 20)
            ellipse(x, y, 20, 20)
    else:
            text("#GAMEOVER", 250, 250)
            text(str(count), 200, 250)
        
            
def mouseClicked():
    global x, y, x_s, y_s, a, b, c, d, e, mode, count
    global hit1, hit2, hit3, hit4, hit5, game
    if mouseX >= 0 and mouseX <= 275:
        global mode
        mode = True
        x, y, x_s, y_s = 275, 470, -5, -3 #Respectively Xposition, Yposition, Xspeed, Yspeed
        a, b, c, d, e = 255, 255, 255, 255, 255 #Brick Colors
        mode, count = True, 0
        hit1, hit2, hit3, hit4, hit5 = True, True, True, True, True
        game = False
    else:
        game = True
    
            
    
        
    
