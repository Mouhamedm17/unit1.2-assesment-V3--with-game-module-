import turtle as trtl
import mPlayer as pl
import mAsteroid as ast
import math as m

  #-------------------Screen variables--------------------------
wn = trtl.Screen()
#wn.bgpic = "Image_spaceBackground.gif"
wn.setup(width=500, height=1000)

#-------------------Turtle timer------------------------------
timer = trtl.Turtle()
timer.hideturtle()
timer.penup()
timer.speed(0)
timer.goto(0,400)

global timerFont
timerFont = ("Ariel", 50, "normal")

#--------------------initialize scorekeeper------------
scoreKeeper = trtl.Turtle()
scoreKeeper.speed(0)
scoreKeeper.penup()
scoreKeeper.hideturtle()

#----------------------timer variables-------------------------
global timer_interval
timer_interval = 1000 # 1000 represents 1 second

leaderboard_file_name = "scores.txt"
#player_name = input("Please enter your name:")

time = 0
score = 0
score == time

lives = 2

#---------------------functions--------------------------------
#keep track of elapsed time
def timeElapsed(): 
    global time 
    timer.clear()
    timer.write("Time:" + str(time), font=timerFont)
    time += 1
    timer.getscreen().ontimer(timeElapsed, timer_interval)

#manages the leaderboard for top 5 scorers
"""def manage_leaderboard():

  global score
  global scoreKeeper

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, scoreKeeper, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, scoreKeeper, score)"""

#end the game if there's been a collision
def collision():
    global lives
    lives -=1

    pl.spaceship.hideturtle()
    ast.asteroid.hideturtle()

#game function
def game():
    playerCoordinates = [pl.spaceship.xcor(), pl.spaceship.ycor()]
    asteroidCoordinates = [ast.asteroid.xcor(), ast.asteroid.ycor()]
    distance = m.dist(playerCoordinates, asteroidCoordinates)

    timeElapsed()
    pl.movement()
    ast.Asteroid()

    if distance > 1:
        print(distance)




#-----------------------commands------------------------------
#game()

#wn.mainloop()

#*****THE FUNCTIONS DON'T RUN AT THE SAME TIME
#look into wn.update() or multithreading