import math
import turtle
import os
import random
#setup screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")
wn.bgpic("bg.png")
wn.setup(width=650,height=650)

#register shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#draw border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(590)
    border_pen.lt(90) #angle
border_pen.hideturtle()

#scoring
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,260)
scorestring="score:%s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal")) 
score_pen.hideturtle()
#create player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed=15



#choose no.of enemies
number_of_enemies=5
#create an empty list of enemies
enemies=[]

#add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())


for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
enemyspeed=2

#create player's bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#bullet states
#ready & fire
bulletstate="ready"

#move player left & right
def move_left():
    x=player.xcor()
    x-=playerspeed   #move 15pixels each tym key pressed
    if x<-280:
        x=-280       #movement within border
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed   #move 15pixels each tym key pressed
    if x>270:
        x=270  
    player.setx(x)  

def fire_bullet():
    #any changes to bulletstate inside this func vl be reflected everywhere else
    global bulletstate
    if bulletstate=="ready":
        os.system("afplay laser.wav&") #if & not used...game pauses vn sound plays
        bulletstate="fire"
        #move bullet just above the player
        x=player.xcor()
        y=player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#use pythogaurus thrm to calc the dist(a^2 + b^2 = c^2)
def isCollision(t1,t2):
    distance =math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False           
     

#keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left") 
turtle.onkey(move_right,"Right")  
turtle.onkey(fire_bullet,"space")

#main loop
while True:
    for enemy in enemies:

        #move enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #move enemy in reverse direction & jump down vn hit border
        if enemy.xcor()>280:
            for e in enemies: 
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
        if enemy.xcor()<-280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1     
        #collision bet bullet & enemy    
        if isCollision(bullet,enemy):
            os.system("afplay explosion.wav&")
            #reset the bullet 
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400) 
            #reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)
            #update score
            score+=10
            scorestring="score:%s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))  
        #collision between player & enemy
        if isCollision(player,enemy):
            os.system("afplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break        

    #move bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
    #check if bullet has gone to the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
    
         
         

    




