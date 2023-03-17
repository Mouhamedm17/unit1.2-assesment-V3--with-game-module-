import turtle as trtl
import random as rand

# --------setup----------
asteroidImage = "Image_asteroidImage.gif"


#--------------initialize screen-----------------------
wn = trtl.Screen()
wn.setup(width=500, height=1000)
wn.addshape(asteroidImage)

#---------------------varaibles------------------------
speed = 1
speedCounter = 1
isHit = False

#---------------initialize asteroid--------------------
asteroid = trtl.Turtle()
def init():
    asteroid.hideturtle()
    asteroid.penup()
    asteroid.shape(asteroidImage)

#---------------functions-----------------

def Asteroid():
    init()
    asteroid.shape(asteroidImage)
    asteroid.hideturtle()
    asteroid.penup()

    falling()
    wn.update()

def falling():
    global speed
    global speedCounter

    while isHit == False:
        asteroid.speed(speed)
        spawnPosition = rand.randint(-250,250)
        
        asteroid.goto(spawnPosition, 500)
        asteroid.showturtle()
        asteroid.goto(spawnPosition, -500)
        asteroid.hideturtle()

        speedCounter +=1

        if speedCounter % 5 == 1:
            speed +=1
    
    Asteroid(asteroid)
    
#----------------commands-----------------
#Asteroid(asteroid)

#wn.mainloop()