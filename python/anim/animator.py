import turtle as t
import time # temporary

def display(val):
    if val:
        t.showturtle()
    else:
        t.hideturtle()
    print(f"Successfully set display() to {val}")

def rCircle(rad, fsize, spacing):
    if rad < 50:
        print(f"error: rad is under 50, with a value of {rad}, correcting to 50")
        rad = 50

    back = rad / 2
    t.circle(rad)
    t.left(90)
    t.forward(rad)
    t.penup()
    t.backward(back)
    t.right(90)
    t.forward(spacing)
    try:
        t.write(str(rad), font=("arial", fsize, "normal"))
    except:
        print(f"error: t.write() failed. With values: fsize={fsize}")
    t.left(90)
    print(f"Successfully performed rCircle() with a radius of {rad}")

def pat(len: int, patNum: int):
    nPat = patNum / 2
    angle = (((nPat - 2) * 180) / nPat)
    while not patNum == 0:
        t.right(angle)
        t.forward(len)
        patNum -= 1
    print(f"Successfully generated a pattern with a seed of {patNum}")

def speed(s):
    t.speed(s)
    print(f"Successfully performed speed() with a input of {s}")