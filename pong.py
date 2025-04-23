import tkinter as tk
import turtle as trtl
import random
import math

# initializing basic variables
paddleVelocity = 9
velocity = 18
angleGoing = 0
wn = trtl.Screen()
lastKeyPress = ""
counter = 0

# decorative shapes
arena = trtl.Turtle()
arena.shape("square")
arena.turtlesize(21)
arena.speed(0)
arena.back(20)

arenaTwo = trtl.Turtle()
arenaTwo.shape("square")
arenaTwo.turtlesize(21)
arenaTwo.speed(0)
arenaTwo.forward(20)

centerline = trtl.Turtle()
centerline.speed(0)
centerline.color("white")
centerline.fillcolor("white")
centerline.pencolor("white")
centerline.pensize(3)
centerline.goto(0, -300)
centerline.goto(0, 300)

middle = trtl.Turtle()
middle.turtlesize(0.5)
middle.shape("circle")
middle.color("white")
middle.fillcolor("white")

# create ball
pongBall = trtl.Turtle()
pongBall.shape("circle")
pongBall.color("white")
pongBall.fillcolor("white")
pongBall.speed(0)
pongBall.penup()

# create left paddle
increment = 0
enemyPaddle = []
for i in range(5):
    newTurtle = trtl.Turtle()
    newTurtle.shape("square")
    newTurtle.fillcolor("red")
    newTurtle.color("red")
    newTurtle.penup()
    newTurtle.speed(0)
    newTurtle.goto(-220, -40 + increment)
    increment += 20
    enemyPaddle.append(newTurtle)

# create right paddle
increment = 0
userPaddle = []
for i in range(5):
    newTurtle = trtl.Turtle()
    newTurtle.shape("square")
    newTurtle.fillcolor("blue")
    newTurtle.color("blue")
    newTurtle.penup()
    newTurtle.speed(0)
    newTurtle.goto(220, -40 + increment)
    increment += 20
    userPaddle.append(newTurtle)

# initialize paddle coordinates
enemyPaddleX = enemyPaddle[2].xcor()
enemyPaddleY = enemyPaddle[2].ycor()

userPaddleX = userPaddle[2].xcor()
userPaddleY = userPaddle[2].ycor()

# initialize ball direction
angleGoing = random.randint(0, 359)
angleGoing = float(math.radians(angleGoing))
xVelocity = float(math.cos(angleGoing) * velocity)
yVelocity = float(math.sin(angleGoing) * velocity)

# used to set random angle for the ball
def RandomAngle(min, max):
    global angleGoing
    global xVelocity
    global yVelocity
    angleGoing = random.randint(min, max)
    angleGoing = float(math.radians(angleGoing))
    xVelocity = float(math.cos(angleGoing) * velocity)
    yVelocity = float(math.sin(angleGoing) * velocity)

def MoveUp():
    global userPaddle
    global userPaddleY
    global lastKeyPress
    global counter
    global xVelocity
    global yVelocity
    global pongBall
    global enemyPaddleX
    global enemyPaddleY
    global userPaddleX
    global userPaddleY
    if (userPaddleY < 150):
        for i in range(len(userPaddle)):
            userPaddle[i].goto(userPaddle[i].xcor(), userPaddle[i].ycor() + paddleVelocity * 2)
    lastKeyPress = "w"
    counter = 7
    # bounce ball off of floor and ceiling
    if (math.fabs(pongBall.ycor()) >= 200):
        yVelocity = yVelocity * -1
        # check if x velocity is too small for the ball to go anywhere, then reset velocity with new angle
        if (math.fabs(xVelocity) <= 3):
            if (yVelocity < 0):
                RandomAngle(210, 330)
            elif (yVelocity > 0):
                RandomAngle(30, 150)
    # check if the paddles are in range of the ball, if they are, bounce the ball back, otherwise, reset ball
    if (math.fabs(pongBall.xcor()) >= 195):
        if (pongBall.xcor() < 0 and math.fabs(enemyPaddleY - pongBall.ycor()) <= 57.5 and pongBall.xcor() > -215):
            xVelocity = xVelocity * -1
            if (xVelocity < 0):
                xVelocity = xVelocity * -1
        elif (pongBall.xcor() > 0 and math.fabs(userPaddleY - pongBall.ycor()) <= 57.5 and pongBall.xcor() < 215):
            xVelocity = xVelocity * -1
            if (xVelocity > 0):
                xVelocity = xVelocity * -1
            elif (counter > 0):
                if ((lastKeyPress == "s" and yVelocity > 0) or (lastKeyPress == "w" and yVelocity < 0)):
                    Flatten()
                    print("flatten")
                elif ((lastKeyPress == "w" and yVelocity > 0) or (lastKeyPress == "s" and yVelocity < 0)):
                    Steepen()
                    print("steepen")
        elif (math.fabs(pongBall.xcor()) >= 225):
            pongBall.goto(0, 0)
            if (xVelocity > 0):
                if (random.randint(1, 2) == 1):
                    RandomAngle (1, 89)
                else:
                    RandomAngle (271, 359)
            else:
                RandomAngle (91, 269)

def MoveDown():
    global userPaddle
    global userPaddleY
    global lastKeyPress
    global counter
    global xVelocity
    global yVelocity
    global pongBall
    global enemyPaddleX
    global enemyPaddleY
    global userPaddleX
    global userPaddleY
    if (userPaddleY > -150):
        for i in range(len(userPaddle)):
            userPaddle[i].goto(userPaddle[i].xcor(), userPaddle[i].ycor() - paddleVelocity * 2)
    lastKeyPress = "s"
    counter = 7
    # bounce ball off of floor and ceiling
    if (math.fabs(pongBall.ycor()) >= 200):
        yVelocity = yVelocity * -1
        # check if x velocity is too small for the ball to go anywhere, then reset velocity with new angle
        if (math.fabs(xVelocity) <= 3):
            if (yVelocity < 0):
                RandomAngle(210, 330)
            elif (yVelocity > 0):
                RandomAngle(30, 150)
    # check if the paddles are in range of the ball, if they are, bounce the ball back, otherwise, reset ball
    if (math.fabs(pongBall.xcor()) >= 195):
        if (pongBall.xcor() < 0 and math.fabs(enemyPaddleY - pongBall.ycor()) <= 57.5 and pongBall.xcor() > -215):
            xVelocity = xVelocity * -1
            if (xVelocity < 0):
                xVelocity = xVelocity * -1
        elif (pongBall.xcor() > 0 and math.fabs(userPaddleY - pongBall.ycor()) <= 57.5 and pongBall.xcor() < 215):
            xVelocity = xVelocity * -1
            if (xVelocity > 0):
                xVelocity = xVelocity * -1
            elif (counter > 0):
                if ((lastKeyPress == "s" and yVelocity > 0) or (lastKeyPress == "w" and yVelocity < 0)):
                    Flatten()
                    print("flatten")
                elif ((lastKeyPress == "w" and yVelocity > 0) or (lastKeyPress == "s" and yVelocity < 0)):
                    Steepen()
                    print("steepen")
        elif (math.fabs(pongBall.xcor()) >= 225):
            pongBall.goto(0, 0)
            if (xVelocity > 0):
                if (random.randint(1, 2) == 1):
                    RandomAngle (1, 89)
                else:
                    RandomAngle (271, 359)
            else:
                RandomAngle (91, 269)

def Flatten():
    global xVelocity
    global yVelocity
    xVelocity = xVelocity * 1.3
    yVelocity = yVelocity * (1/1.3)

def Steepen():
    global xVelocity
    global yVelocity
    xVelocity = xVelocity * (1/1.3)
    yVelocity = yVelocity * 1.3

while True:
    # keep updating positions for both paddles
    enemyPaddleX = enemyPaddle[2].xcor()
    enemyPaddleY = enemyPaddle[2].ycor()
    userPaddleX = userPaddle[2].xcor()
    userPaddleY = userPaddle[2].ycor()

    counter -= 1

    # automatically move enemy paddle towards ball's y-coordinate
    if (enemyPaddleY < pongBall.ycor() and enemyPaddleY < 160):
        for i in range(len(enemyPaddle)):
            enemyPaddle[i].goto(enemyPaddle[i].xcor(), enemyPaddle[i].ycor() + paddleVelocity)
    elif (enemyPaddleY > pongBall.ycor() and enemyPaddleY > -160):
        for i in range(len(enemyPaddle)):
            enemyPaddle[i].goto(enemyPaddle[i].xcor(), enemyPaddle[i].ycor() - paddleVelocity)
    # move ball
    pongBall.goto(pongBall.xcor() + xVelocity, pongBall.ycor() + yVelocity)
    # bounce ball off of floor and ceiling
    if (math.fabs(pongBall.ycor()) >= 200):
        yVelocity = yVelocity * -1
        # check if x velocity is too small for the ball to go anywhere, then reset velocity with new angle
        if (math.fabs(xVelocity) <= 3):
            if (yVelocity < 0):
                RandomAngle(210, 330)
            elif (yVelocity > 0):
                RandomAngle(30, 150)
    # check if the paddles are in range of the ball, if they are, bounce the ball back, otherwise, reset ball
    if (math.fabs(pongBall.xcor()) >= 195):
        if (pongBall.xcor() < 0 and math.fabs(enemyPaddleY - pongBall.ycor()) <= 57.5 and pongBall.xcor() > -215):
            xVelocity = xVelocity * -1
            if (xVelocity < 0):
                xVelocity = xVelocity * -1
        elif (pongBall.xcor() > 0 and math.fabs(userPaddleY - pongBall.ycor()) <= 57.5 and pongBall.xcor() < 215):
            xVelocity = xVelocity * -1
            if (xVelocity > 0):
                xVelocity = xVelocity * -1
            elif (counter > 0):
                if ((lastKeyPress == "s" and yVelocity > 0) or (lastKeyPress == "w" and yVelocity < 0)):
                    Flatten()
                elif ((lastKeyPress == "w" and yVelocity > 0) or (lastKeyPress == "s" and yVelocity < 0)):
                    Steepen()
        elif (math.fabs(pongBall.xcor()) >= 225):
            pongBall.goto(0, 0)
            if (xVelocity > 0):
                if (random.randint(1, 2) == 1):
                    RandomAngle (1, 89)
                else:
                    RandomAngle (271, 359)
            else:
                RandomAngle (91, 269)

    wn.onkeyrelease(MoveUp, "w")
    wn.onkeyrelease(MoveDown, "s")
    wn.listen()