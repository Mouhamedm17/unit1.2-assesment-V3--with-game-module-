#import asteroid as ast
import turtle as trtl
#mport game as gm
#import math as m
#import leaderboard as lb
import threading

#-------------------variables--------------------------
spaceshipImage = "Image_spaceship.gif"
displacement = 20
leftBorderLimit = -250
rightBorderLimit = 250
heightLimit = 500
baseLimit = -500

#-------------------initialize the turtles-------------
spaceship = trtl.Turtle()
spaceship.hideturtle()

#------------------initialize screen-------------------
wn = trtl.Screen()
wn.setup(width=500, height=1000)
wn.addshape(spaceshipImage)

#---------------------initialize player----------------
def playerInit():
    spaceship.penup()
    spaceship.goto(0,-500)
    spaceship.shape(spaceshipImage)
    spaceship.showturtle()
    spaceship.speed(9)

#---------------------functions------------------------
def forward():
    spaceship.setheading(90)
    spaceship.forward(displacement)

    if spaceship.ycor() >= heightLimit:
        spaceship.hideturtle()
        spaceship.goto(spaceship.xcor(), -spaceship.ycor())
        spaceship.showturtle()

def backward():
    spaceship.setheading(270)
    spaceship.forward(displacement)

    if spaceship.ycor() <= (baseLimit):
        spaceship.hideturtle()
        spaceship.goto(spaceship.xcor(), -spaceship.ycor())
        #spaceship.goto(spaceship.xcor, 500-spaceship.ycor())
        spaceship.showturtle()

def left():
    spaceship.setheading(180)
    spaceship.forward(displacement)

    if spaceship.xcor() <= leftBorderLimit:
        spaceship.hideturtle()
        spaceship.goto(-spaceship.xcor(), spaceship.ycor())
        spaceship.showturtle()

def right():
    spaceship.setheading(0)
    spaceship.forward(displacement)

    if spaceship.xcor() >= rightBorderLimit:
        spaceship.hideturtle()
        spaceship.goto(-spaceship.xcor(), spaceship.ycor())
        spaceship.showturtle()

#general movement function
def movement():
    playerInit()
    wn.onkeypress(forward, "Up")
    wn.onkeypress(backward, "Down")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")
    wn.listen()

#------------------------commands-----------------------------------
#movement()

#wn.mainloop()