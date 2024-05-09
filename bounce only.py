#import turtle
import turtle
turtle.getscreen()
turtle.bgcolor("black")
turtle.title("Bouncing ball")

#make the ball and put it in the middle of the screen
ball = turtle.Turtle()
ball.shape("circle")
ball.color("lime green")
ball.penup()
ball.speed(0)
ball.goto(0,300)


ground = -350


t=0

 
falling = True
while falling:
    ball.sety (300+(((-0.981 * t**2)/2)))

    if ball.ycor() < ground:
        falling = False
        vf = 0.981 * t 
    t += 1

v = vf
t = 0

bouncing = True
while bouncing:
    ball.sety((v * t - (0.981 * t **2)) + ground)
  
    if ball.ycor() < ground:
        v = v * 0.82
        if v < 0.981:
            bouncing = False
        t=0
       
    
    t += 1
    
    
