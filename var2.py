from tkinter import *
from array import array

# Define uri

arr = []   
ok = 0

def onClick(args):
    global ok
    arr.append(args)
    print(arr)
    T.delete('1.0',END)
    if ok == 0:
      T.insert(END,"""           
      Care vrei  sa fie fundalul actiunii?
      Apasa unul din butoanele de mai jos pentru a selecta raspunsul!
    
        """)
      ok = 1
    if ok == 1:
        T.insert(END,"""           
      cf?
      Apasa unul din butoanele de mai jos pentru a selecta raspunsul!
    
        """)


# Rooturi
root = Tk()
root.title("GUI Button")
frametop = Frame(root)
framebottom = Frame(root)
frame1 = Frame(framebottom)
frame2 = Frame(framebottom)



# Text

T = Text(frametop, height=4, width=75)
T.insert(END,"""           
      Unde vrei sa aiba loc actiunea?
      Apasa unul din butoanele de mai jos pentru a selecta raspunsul!
        
        """)

# Butoane
btn1 = Button(frame1, text="Choice 1", padx = 40, pady = 20, command=lambda:onClick(1))
btn2 = Button(frame2, text="Choice 2", padx = 40, pady = 20, command=lambda:onClick(2))


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

# codul 2

import turtle as tr
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
    tr.color("black")
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
    tr.color("yellow")
    tr.begin_fill()
    for i in range(5):
        tr.forward(10)
        tr.right(144)
    tr.end_fill()

# Draw multiple stars at random locations on the screen
    for i in range(20):
        x = rand.randint(-400, 400)
        y = rand.randint(-250, 250)
        star()
        tr.penup()
        tr.goto(x, y)
        tr.pendown()

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


def layer1():
    tr.speed(0)
    tr.bgcolor("lightblue")
    drawcloudy()
    drawsun(250, 150)
    drawfields()
    drawtree(-200, -100)
    drawtree(250, -100)
    stickman(-100, -150)
    stickman(-120, -300)
    stickman(100, -150)
    stickman(120, -300)

layer1()
tr.done()
