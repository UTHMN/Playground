import turtle as t
import time # temporary

def display(true):
    if true:
        t.showturtle()
    else:
        t.hideturtle()

def rCircle(rad, font, fsize, spacing):
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
        t.write("r", font=(font, fsize, "normal"))
    except:
        print(f"error: t.write() failed. With values: font={font}, fsize={fsize}")
    t.left(90)
    print(f"Successfully performed rCircle() with a radius of {rad}")

def shape(len: int, sides: int):
    angle = (((sides - 2) * 180) / sides)
    while not sides == 0:
        t.right(angle)
        t.forward(len)
        sides -= 1 

display(True)
# ((sides - 2) * 180) / sides
shape(150, 6)