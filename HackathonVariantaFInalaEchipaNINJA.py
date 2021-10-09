from tkinter import *
from array import array

# Define uri

arr = []   
ok = 0


def onClick(args):
    global ok
    global root
    arr.append(args)
#   print(arr)
    T.delete('1.0',END)
    if ok == 0:
      T.insert(END,"""           
      Unde vrei să mergem?
      Opțiunea 1: În oraș    Opțiunea 2: În natură
      Apasă unul din butoanele de mai jos pentru a selecta răspunsul!
      Vă recomandăm să încercați toate variantele! ( 2 ^ 3 = 8 variante)
        """)
      ok = 1
    elif ok == 1:
        T.insert(END,"""           
      Cum vrei să comunicăm?
      Opțiunea 1: Jucând fotbal    Opțiunea 2: Plimbându-ne 
      Apasă unul din butoanele de mai jos pentru a selecta răspunsul!
      Vă recomandăm să încercați toate variantele! ( 2 ^ 3 = 8 variante)
        """)
        ok = 2
    elif ok == 2:
        root.destroy()


# Rooturi
root = Tk()
root.title("GUI Button")
frametop = Frame(root)
framebottom = Frame(root)
frame1 = Frame(framebottom)
frame2 = Frame(framebottom)

# Text

T = Text(frametop, height=6, width=75)
T.insert(END,"""           
      Când te simți mai bine?
      Opțiunea 1: Dimineața    Opțiunea 2: Seara
      Apasă unul din butoanele de mai jos pentru a selecta răspunsul!
      Vă recomandăm să încercați toate variantele!(2 ^ 3 = 8 variante)        
        """)

# Butoane
btn1 = Button(frame1, text="Opțiunea 1", padx = 40, pady = 20, command=lambda:onClick(1))
btn2 = Button(frame2, text="Opțiunea 2", padx = 40, pady = 20, command=lambda:onClick(2))

# packuri frame
frametop.pack(side=TOP, fill=BOTH, expand=1)
framebottom.pack(side=BOTTOM, fill=BOTH, expand=1)
frame1.pack(side=LEFT, fill=BOTH, expand=1)
frame2.pack(side=RIGHT, fill=BOTH, expand=1)

# packuri aditionale
T.pack()
btn1.pack(side=TOP, fill=BOTH, padx=100, pady=40, expand=1)
btn2.pack(side=TOP, fill=BOTH, padx=100, pady=40, expand=1) 

root.mainloop()

import turtle as tr
import tkinter as tk
import math
import random as rand

tr.speed(6)
tr.hideturtle()

def drawscircle(y, x, rang):
    tr.speed(0)
    for i in range(1, math.ceil(rang / 5)):
        tr.penup()
        tr.goto(y, x - i * 5)
        tr.pendown()
        tr.circle(i * 5)
    tr.speed(6)

def drawfcircle(y, x, rang):
    tr.penup()
    tr.goto(y, x)
    tr.pendown()
    tr.begin_fill()
    tr.circle(rang)
    tr.end_fill()

def drawcloud(y, x):
    tr.penup()
    tr.goto(y, x)
    tr.color("#eeeeee")
    drawfcircle(y-10, x+10, 30)
    drawfcircle(y + 30, x + 10, 50)
    drawfcircle(y + 73, x + 20, 20)
    

def drawcloudy():
    drawcloud(-200, 100)
    drawcloud(-300, 200)
    drawcloud(0, 200)

def drawsun(y, x):
    tr.speed(0)
    tr.penup()
    tr.goto(y, x)
    tr.pendown()
    tr.color("yellow")
    for i in range(200):
        tr.left(i)
        tr.forward(i * 1.2)
    tr.penup()
    tr.home()

def drawfields():
    #tr.speed(0)
    tr.color("#1C7947")
    drawfcircle(300, -800, 400)
    tr.color("#39A388")
    drawfcircle(-300, -1000, 500)
    tr.penup()

def tree(i):
    if i<10:
        return
    else:
        tr.fd(i)
        tr.lt(30)
        tree(3*i/3.8)
        tr.right(60)
        tree(3*i/3.8)
        tr.left(30)
        tr.backward(i)

def drawtree(y, x):
    tr.home()
    tr.penup()
    tr.goto(y, x)
    tr.pendown()
    tr.color("brown")
    tr.left(90)
    tr.speed(0)
    tree(70)

def stickman(y, x):
    tr.color("white")
    tr.penup()
    tr.goto(y + 50, x)
    tr.pendown()
    tr.goto(y, x + 50)
    tr.goto(y - 50, x)
    tr.goto(y, x + 50)
    tr.goto(y, x + 100)
    tr.goto(y + 50, x + 50)
    tr.goto(y, x + 100)
    tr.goto(y - 50, x + 50)
    tr.goto(y, x + 100)
    drawfcircle(y, x + 100, 20)


def star():
    x = rand.randint(-300, 400)
    y = rand.randint(100, 300)
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.color("yellow")
    tr.begin_fill()
    for i in range(5):
        tr.forward(10)
        tr.right(144)
    tr.end_fill()
       

def moon():
    tr.penup()
    tr.goto(-300, 100)
    tr.pendown()
    tr.color("white")
    tr.begin_fill()
    tr.circle(50)
    tr.end_fill()
    tr.penup()
    tr.goto(-280, 100)
    tr.pendown()
    tr.color("black")
    tr.begin_fill()
    tr.circle(50)
    tr.end_fill()

def bloc():
    # Dome
    tr.penup()
    tr.goto(-150, 20)
    tr.pendown()
    tr.color("saddlebrown")
    tr.begin_fill()
    tr.circle(100)
    tr.end_fill()

def pull():
# Bottom rectangle
    tr.penup()
    tr.goto(-350, -200)
    tr.pendown()
    tr.begin_fill()
    for i in range(2):
        tr.forward(400)
        tr.left(90)
        tr.forward(20)
        tr.left(90)
    tr.end_fill()

# Second from bottom rectangle
    tr.penup()
    tr.goto(-325, -180)
    tr.pendown()
    tr.color("chocolate")
    tr.begin_fill()
    for i in range(2):
        tr.forward(350)
        tr.left(90)
        tr.forward(20)
        tr.left(90)
    tr.end_fill()

# Main part of building
    tr.penup()
    tr.goto(-300, -160)
    tr.pendown()
    tr.color("sandybrown")
    tr.begin_fill()
    for i in range(2):
        tr.forward(300)
        tr.left(90)
        tr.forward(250)
        tr.left(90)
    tr.end_fill()

# Second from top rectangle
    tr.penup()
    tr.goto(-325, 90)
    tr.pendown()
    tr.color("chocolate")
    tr.begin_fill()
    for i in range(2):
        tr.forward(350)
        tr.left(90)
        tr.forward(20)
        tr.left(90)
    tr.end_fill()

    # Top rectangle
    tr.penup()
    tr.goto(-300, 110)
    tr.pendown()
    tr.color("sienna")
    tr.begin_fill()
    for i in range(2):
        tr.forward(300)
        tr.left(90)
        tr.forward(20)
        tr.left(90)
    tr.end_fill()

    # Windows
    x = -275
    y = 30
    tr.color("khaki")

    # Draw a single window_height
    def window(x):
        tr.penup()
        tr.goto(x, y)
        tr.pendown()
        tr.begin_fill()
        for i in range(4):
            tr.forward(40)
            tr.left(90)
        tr.end_fill()

    # Draw the windows
    for i in range(3): # This loop will draw 3 rows of windows
        for j in range(4): # This loop will draw one row of 4 windows
            window(x + j * 70)
        x = -275 # Ensures all rows of windows start from the same x-position
        y = y - 85 # Moves the next row of windows down lower than the previous


def goal(y, x):
    tr.color("white")
    tr.penup()
    tr.goto(y, x)
    tr.pendown()
    tr.goto(y + 50, x + 200)
    tr.goto(y, x)
    tr.goto(y + 50, x)
    tr.goto(y, x + 200)
    tr.goto(y + 50, x)
    tr.goto(y + 50, x + 200)
    tr.goto(y, x + 200)
    tr.goto(y, x)

def layer1():
    tr.speed(0)
    tr.bgcolor("lightblue")
    drawcloudy()
    #drawsun(250, 150)
    drawfields()
    #drawtree(-200, -100)
    #drawtree(250, -100)
    stickman(-100, -150)
    stickman(-120, -300)
    stickman(100, -150)
    stickman(120, -300)
    goal(-370, -300)
    goal(310, -300)
    tr.color("white")
    drawfcircle(0, -200, 30)
    tr.color("blue")
    drawscircle(0, -170, 30)

#layer1()

def layer2():
    tr.speed(0)
    tr.bgcolor("black")
    #for i in range(30):
        #star()
    moon()
    bloc()
    pull()

def maintr():
    if arr[0] == 1:
        tr.speed(0)
        tr.bgcolor("lightblue")
        drawcloudy()
        drawsun(250, 150)
    else:
        tr.speed(0)
        tr.bgcolor("black")
        for i in range(30):
            star()
        moon()
    if arr[1] == 1:
        tr.penup()
        tr.color("gray")
        tr.begin_fill()
        tr.goto(-600, -500)
        tr.goto(600, -500)
        tr.goto(600, 0)
        tr.goto(-600, 0)
        tr.goto(-600, -500)
        tr.end_fill();
        bloc()
        pull()
    else: 
        drawfields()
        drawtree(-200, -100)
        tr.penup()
        drawtree(250, -100)
        tr.penup()
        tr.home()
        tr.penup()
    if arr[2] == 1:
        if arr[1] == 2:
            stickman(-100, -150)
        stickman(-120, -300)
        stickman(100, -150)
        stickman(120, -300)
        goal(-370, -300)
        goal(310, -300)
        tr.color("white")
        drawfcircle(0, -200, 30)
        tr.color("blue")
        drawscircle(0, -170, 30)
    else: 
        if arr[1] == 2:
            stickman(-100, -150)
        stickman(-120, -300)
        stickman(100, -150)
        stickman(120, -300)

maintr()
tr.done()

