import tkinter as tk
import turtle as trtl
import random
import math

velocity = 6
angleGoing = 0

pongBall = trtl.Turtle()
pongBall.shape("circle")
pongBall.forward(3)
pongBall.speed(0)
pongBall.penup()

increment = 0
enemyPaddle = []
for i in range(5):
    newTurtle = trtl.Turtle()
    newTurtle.shape("square")
    newTurtle.penup()
    newTurtle.speed(0)
    newTurtle.goto(-220, -40 + increment)
    increment += 20
    enemyPaddle.append(newTurtle)

enemyPaddleX = enemyPaddle[2].xcor()
enemyPaddleY = enemyPaddle[2].ycor()

angleGoing = random.randint(0, 359)
angleGoing = float(math.radians(angleGoing))
xVelocity = float(math.cos(angleGoing) * velocity)
yVelocity = float(math.sin(angleGoing) * velocity)

while True:
    enemyPaddleX = enemyPaddle[2].xcor()
    enemyPaddleY = enemyPaddle[2].ycor()
    if (enemyPaddleY < pongBall.ycor()):
        for i in range(len(enemyPaddle)):
            enemyPaddle[i].goto(enemyPaddle[i].xcor(), enemyPaddle[i].ycor() + 2)
    elif (enemyPaddleY > pongBall.ycor()):
        for i in range(len(enemyPaddle)):
            enemyPaddle[i].goto(enemyPaddle[i].xcor(), enemyPaddle[i].ycor() - 2)
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
        if (pongBall.xcor() < 0 and math.fabs(enemyPaddleY - pongBall.ycor()) <= 52):
            xVelocity = xVelocity * -1
        else:
            pongBall.goto(0, 0)
            angleGoing = random.randint(0, 359)
            angleGoing = float(math.radians(angleGoing))
            xVelocity = float(math.cos(angleGoing) * velocity)
            yVelocity = float(math.sin(angleGoing) * velocity)

            


tk.mainloop()