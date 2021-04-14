#idek what im doing at this point there has to be a way better way of doing this but idk it

import turtle
import random
import time


window = turtle.Screen()
t = turtle.Turtle() 

x = -350
y = 225

xnum = 75
ynum = 0

rolling = bool
diceNum = 0
moving = False

canSpace = True
canEnter = False

entered = False

t.speed(0)

def drawBoard():
  t.penup()
  t.goto(-275, 150)

  t.color('black')
  t.pendown()
  for i in range(2):
    t.forward(525)
    t.right(90)
    t.forward(300)
    t.right(90)

  t.penup()
  t.goto(-350, 225)
  t.color('black')
  t.pendown()
  for i in range(2):
    t.forward(675)
    t.right(90)
    t.forward(450)
    t.right(90)
  t.penup()

def moveTiles():
  global x
  global y
  global xnum
  global ynum
  x += xnum
  y += ynum

  
def drawTile(color):
  t.penup()
  t.goto(x, y)
  t.color(color)
  t.pendown()
  t.begin_fill()
  for i in range(2):
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(90)
  t.end_fill()
  t.color('black')
  for i in range(2):
    t.forward(75)
    t.right(90)
    t.forward(75)
    t.right(90)
  t.penup()

  moveTiles()

def drawTiles():
  global xnum
  global ynum

  drawTile("magenta")
  drawTile("green")
  drawTile("blue")
  drawTile("red")
  drawTile("blue")
  drawTile("red")
  drawTile("blue")
  drawTile('blue')
  xnum = 0
  ynum = -75
  drawTile("magenta")
  drawTile('blue')
  drawTile('brown')
  drawTile('blue')
  drawTile('blue')
  xnum = -75
  ynum = 0
  drawTile('brown')
  drawTile('red')
  drawTile('blue')
  drawTile('red')
  drawTile("magenta")
  drawTile('red')
  drawTile('brown')
  drawTile("magenta")
  xnum = 0
  ynum = 75
  drawTile("magenta")
  drawTile("magenta")
  drawTile("magenta")
  drawTile("magenta")
  drawTile("magenta")



piece = turtle.Turtle()
piece.shape("turtle")
piece.penup()
piece.goto(-250, 200)
piece.setheading(90)
piece.color("black")

piece2 = turtle.Turtle()
piece2.shape("turtle")
piece2.penup()
piece2.goto(-225, 175)
piece2.setheading(90)
piece2.color("grey")


move_speed = 10
turn_speed = 10

def forward():
  piece.forward(move_speed)
def backward():
  piece.backward(move_speed)
def right():
  piece.right(turn_speed)
def left():
  piece.left(turn_speed)

def up():
  piece2.forward(move_speed)
def down():
  piece2.backward(move_speed)
def rt():
  piece2.right(turn_speed)
def lt():
  piece2.left(turn_speed)

#Moves the Turtle
window.onkey(forward,"Up")
window.onkey(backward,"Down")
window.onkey(left,"Left")
window.onkey(right,"Right")

window.onkey(up,"w")
window.onkey(down,"s")
window.onkey(lt,"a")
window.onkey(rt,"d")

window.listen()


drawBoard()
drawTiles()
t.hideturtle() 


dice = turtle.Turtle()
dice.hideturtle()
dice.penup()
dice.color("green")
dice.goto(-100,-100)
dice.pendown()



def rng():
  global rolling
  global diceNum
  global canSpace

  if canSpace == True:
    canSpace = False
    dice.clear()
    rolling = True
    for i in range(9):
      dice.clear()
      diceNum = (str(random.randint(1, 8)))
      dice.write("rolling :  " + str(diceNum), font = ("comic sans", 21))
      time.sleep(.2)
      
    dice.clear()
    diceNum = (str(random.randint(1, 8)))
    dice.write("rolling :  " + str(diceNum), font = ("comic sans", 21))
    time.sleep(1)
    dice.clear()

    rolling = False


def enterPress():
  global entered
  global moving
  global canEnter

  if canEnter == True:

    moving = False
    canEnter = False
    entered = True
    time.sleep(.2)
    entered = False

    intro()
  


def intro():
  global canSpace
  dice.write("press space to roll", font = ("comic sans", 21))
  canSpace = True

def test():
  print(str(canEnter))

window.onkey(rng,"space")
window.onkey(enterPress, "enter")
window.onkey(test, "b")

window.listen()



def rollingCheck():
  global diceNum
  global rolling
  global moving

  if(rolling == False):
    dice.clear
    dice.write("you got a " + str(diceNum) + "!", font = ("comic sans", 21))
    time.sleep(3)
    dice.clear()
    rolling = bool
    moving = True
  
  else:
    pass

def movingCheck():
  global diceNum
  global moving
  global canEnter

  if moving == True:
    canEnter = True
    dice.penup()
    dice.goto(-175,-100)
    dice.pendown()
    dice.write("press enter after moving " + str(diceNum) + " places", font = ("comic sans", 21))

  elif moving == False:
    pass


  if (entered == True):
    dice.clear()


instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.color("black")
instructions.goto(-225,100)
instructions.pendown()

instructions.write("pink is 10 points,", font = ("comic sans", 15)) 
instructions.penup()
instructions.goto(-225,80)
instructions.pendown()
instructions.write("blue is 5 points,", font = ("comic sans", 15)) 
instructions.penup()
instructions.goto(-225,60)
instructions.pendown()
instructions.write("red is -5 points,", font = ("comic sans", 15)) 
instructions.penup()
instructions.goto(-225,40)
instructions.pendown()
instructions.write("and brown is go back to the start", font = ("comic sans", 15)) 
instructions.penup()
instructions.goto(-225,15)
instructions.pendown()
instructions.write("take turns rolling and whoever gets more points wins!", font = ("comic sans", 15)) 



intro()
while True:
  rollingCheck()
  movingCheck()

