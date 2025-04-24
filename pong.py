import tkinter as tk
import turtle as trtl
import random
import math
import time

# initializing basic variables
paddleVelocity = 9
velocity = 18
angleGoing = 0
wn = trtl.Screen()
lastKeyPress = ""
counter = 0
enemyPaddleFreezeRadInitial = float(50/3)
enemyPaddleFreezeRad = enemyPaddleFreezeRadInitial

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
centerline.shape("square")
centerline.shapesize(stretch_wid=20, stretch_len=0.06)

middle = trtl.Turtle()
middle.turtlesize(0.5)
middle.shape("circle")
middle.color("white")
middle.fillcolor("white")

# create left paddle
enemyPaddle = trtl.Turtle()
enemyPaddle.shape("square")
enemyPaddle.fillcolor("red")
enemyPaddle.color("red")
enemyPaddle.penup()
enemyPaddle.speed(0)
enemyPaddle.goto(-220, 0)
enemyPaddle.shapesize(stretch_wid = 5, stretch_len = 1)

# create right paddle
userPaddle = trtl.Turtle()
userPaddle.shape("square")
userPaddle.fillcolor("blue")
userPaddle.color("blue")
userPaddle.penup()
userPaddle.speed(0)
userPaddle.goto(220, 0)
userPaddle.shapesize(stretch_wid = 5, stretch_len = 1)

# create ball
pongBall = trtl.Turtle()
pongBall.shape("circle")
pongBall.color("white")
pongBall.fillcolor("white")
pongBall.speed(0)
pongBall.penup()

# create direction indicator
dirIndicator = trtl.Turtle()
dirIndicator.fillcolor("red")
dirIndicator.color("red")
dirIndicator.pencolor("red")
dirIndicator.pensize(6)
dirIndicator.turtlesize(0.01)
dirIndicator.speed(0)

# initialize paddle coordinates
enemyPaddleX = enemyPaddle.xcor()
enemyPaddleY = enemyPaddle.ycor()

userPaddleX = userPaddle.xcor()
userPaddleY = userPaddle.ycor()

# initialize ball direction
if (random.randint(1, 2) == 1):
    angleGoing = random.randint(40, 140)
else:
    angleGoing = random.randint(220, 320)
dirIndicator.seth(angleGoing)
dirIndicator.penup()
dirIndicator.forward(13)
dirIndicator.pendown()
dirIndicator.forward(40)
dirIndicator.turtlesize(2)
dirIndicator.penup()
dirIndicator.forward(12)
angleGoing = float(math.radians(angleGoing))
xVelocity = float(math.cos(angleGoing) * velocity)
yVelocity = float(math.sin(angleGoing) * velocity)

# used to set random angle for the ball
def RandomAngle(min, max):
    global angleGoing
    global xVelocity
    global yVelocity
    angleGoing = random.randint(min, max)
    dirIndicator.goto(pongBall.xcor(), pongBall.ycor())
    dirIndicator.seth(angleGoing)
    dirIndicator.forward(13)
    dirIndicator.pendown()
    dirIndicator.forward(40)
    dirIndicator.turtlesize(2)
    dirIndicator.penup()
    dirIndicator.forward(12)
    angleGoing = float(math.radians(angleGoing))
    xVelocity = float(math.cos(angleGoing) * velocity)
    yVelocity = float(math.sin(angleGoing) * velocity)

def MoveUp():
    global userPaddle
    global lastKeyPress
    global counter
    global userPaddleX
    global userPaddleY
    if (counter <= 3):
        if (userPaddleY < 150):
            userPaddle.goto(userPaddle.xcor(), userPaddle.ycor() + paddleVelocity * 1.5)
        lastKeyPress = "w"
        counter = 4
    
    userPaddleX = userPaddle.xcor()
    userPaddleY = userPaddle.ycor()

def MoveDown():
    global userPaddle
    global lastKeyPress
    global counter
    global userPaddleX
    global userPaddleY
    if (counter <= 3):
        if (userPaddleY > -150):
            userPaddle.goto(userPaddle.xcor(), userPaddle.ycor() - paddleVelocity * 1.5)
        lastKeyPress = "s"
        counter = 4
    
    userPaddleX = userPaddle.xcor()
    userPaddleY = userPaddle.ycor()

def Flatten():
    global xVelocity
    global yVelocity
    xVelocity = xVelocity * 1.5
    yVelocity = yVelocity / 1.3

def Steepen():
    global xVelocity
    global yVelocity
    xVelocity = xVelocity / 1.3
    yVelocity = yVelocity * 1.5

wn.onkeypress(MoveUp, "Up")
wn.onkeypress(MoveDown, "Down")
wn.listen()

time.sleep(1.5)

while True:
    wn.update()
    time.sleep(float(1/30))

    # keep updating positions for both paddles
    enemyPaddleX = enemyPaddle.xcor()
    enemyPaddleY = enemyPaddle.ycor()

    counter -= 1

    if (yVelocity > velocity * 0.7):
        enemyPaddleFreezeRad = (enemyPaddleFreezeRadInitial * enemyPaddleFreezeRadInitial) / yVelocity

    dirIndicator.turtlesize(0.01)
    dirIndicator.penup()
    dirIndicator.goto(0, 500)

    # automatically move enemy paddle towards ball's y-coordinate
    if (math.fabs(enemyPaddleY - pongBall.ycor()) > enemyPaddleFreezeRad):
        if (enemyPaddleY < pongBall.ycor() and enemyPaddleY < 150):
            enemyPaddle.goto(enemyPaddle.xcor(), enemyPaddle.ycor() + paddleVelocity)
        elif (enemyPaddleY > pongBall.ycor() and enemyPaddleY > -150):
            enemyPaddle.goto(enemyPaddle.xcor(), enemyPaddle.ycor() - paddleVelocity)
    # move ball
    pongBall.goto(pongBall.xcor() + xVelocity, pongBall.ycor() + yVelocity)
    # bounce ball off of floor and ceiling
    if (math.fabs(pongBall.ycor()) >= 200 and pongBall.ycor()/yVelocity > 0):
        yVelocity = yVelocity * -1
        pongBall.goto(pongBall.xcor(), 200 * -(yVelocity/(math.fabs(yVelocity))))
        # check if x velocity is too small for the ball to go anywhere, then reset velocity with new angle
        if (math.fabs(xVelocity) <= 3):
            if (yVelocity < 0):
                RandomAngle(210, 330)
                time.sleep(0.75)
            elif (yVelocity > 0):
                RandomAngle(30, 150)
                time.sleep(0.75)
    # check if the paddles are in range of the ball, if they are, bounce the ball back, otherwise, reset ball
    if (math.fabs(pongBall.xcor()) >= 200):
        if (pongBall.xcor() < 0 and math.fabs(enemyPaddleY - pongBall.ycor()) <= 55):
            xVelocity = xVelocity * -1
            pongBall.setx(-200)
            if (xVelocity < 0):
                xVelocity = xVelocity * -1
        elif (pongBall.xcor() > 0 and math.fabs(userPaddleY - pongBall.ycor()) <= 55):
            pongBall.setx(200)
            if (xVelocity > 0):
                xVelocity = xVelocity * -1
            if (counter > 0):
                if ((lastKeyPress == "s" and yVelocity > 0) or (lastKeyPress == "w" and yVelocity < 0)):
                    Flatten()
                elif ((lastKeyPress == "w" and yVelocity > 0) or (lastKeyPress == "s" and yVelocity < 0)):
                    Steepen()
        elif (math.fabs(pongBall.xcor()) >= 220):
            pongBall.goto(0, 0)
            enemyPaddle.sety(0)
            userPaddle.sety(0)
            if (xVelocity > 0):
                if (random.randint(1, 2) == 1):
                    RandomAngle (20, 70)
                else:
                    RandomAngle (290, 340)
            else:
                RandomAngle (110, 250)
            time.sleep(2)