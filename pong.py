import tkinter as tk
import turtle as trtl
import random
import math

velocity = 3
angleGoing = 0

pongBall = trtl.Turtle()
pongBall.shape("circle")
pongBall.forward(3)
pongBall.speed(0)
pongBall.penup()

angleGoing = random.randint(0, 359)
angleGoing = float(math.radians(angleGoing))
xVelocity = float(math.cos(angleGoing) * velocity)
yVelocity = float(math.sin(angleGoing) * velocity)

while True:
    pongBall.goto(pongBall.xcor() + xVelocity, pongBall.ycor() + yVelocity)
    if (math.fabs(pongBall.ycor()) >= 200):
        yVelocity = yVelocity * -1
        if (math.fabs(xVelocity) <= 0.1):
            if (yVelocity < 0):
                angleGoing = random.randint(181, 359)
            elif (yVelocity > 0):
                angleGoing = random.randint(1, 179)
            angleGoing = float(math.radians(angleGoing))
            xVelocity = float(math.cos(angleGoing) * velocity)
            yVelocity = float(math.sin(angleGoing) * velocity)
    elif (math.fabs(pongBall.xcor()) >= 200):
        xVelocity = xVelocity * -1
            


tk.mainloop()