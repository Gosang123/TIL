import turtle as t
import random


size = 50
color = ["red", "pink", "green", "blue", "black"]


def draw_dot(x,y):
    t.up()
    t.goto(x,y)
    t.dot(size)
    

def draw_triangle(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(360/3)
    t.end_fill()
    
def draw_square(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.setheading(random.randint(0,360))
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(360/4)
    t.end_fill()

def rand_color():
    t.color(random.choice(color))

def size_up():
    global size
    if size >10:
        size+=10

def size_down():
    global size
    if size >10:
        size-=10

t.bgcolor("ivory")
t.speed(0)
t.onscreenclick(draw_dot, 1) # 마우스 왼쪽 클릭
t.onscreenclick(draw_triangle, 2)  #마우스 휠  
t.onscreenclick(draw_square, 3) #마우스 오른쪽 클릭

t.onkeypress(rand_color,"space")
t.onkeypress(size_up,"Up")
t.onkeypress(size_down,"Down")
t.listen()
