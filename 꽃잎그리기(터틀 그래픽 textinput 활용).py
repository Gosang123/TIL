import turtle as t
import random

t.bgcolor("ivory")
t.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b


def petal():
    for i in range(2):
        t.circle(150, 110)
        t.left(70)


def draw_flower():
    t.color(random_color())
    t.begin_fill()
    for i in range(6):
        petal()
        t.left(360/6)
    t.end_fill()


    t.goto(0,-30)
    t.color(random_color())
    t.begin_fill()
    t.circle(30)
    t.end_fill()

t.ht()
draw_flower()
