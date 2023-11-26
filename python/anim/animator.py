import turtle as t

global mPen
mPen = "pendown"

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
    t.pendown()
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
    t.pendown()
    pPat = patNum
    nPat = patNum / 2
    angle = (((nPat - 2) * 180) / nPat)
    while not patNum == 0:
        t.right(angle)
        t.forward(len)
        patNum -= 1
    t.penup()
    print(f"Successfully generated a pattern with a seed of {pPat}")

def speed(s):
    t.speed(s)
    print(f"Successfully performed speed() with a input of {s}")

def left(dir):
    t.left(dir)
    print(f"Successfully performed left() with an input of {dir}")

def right(dir):
    t.right(dir)
    print(f"Successfully performed right() with an input of {dir}")
    
def forward(px):
    t.forward(px)
    print(f"Successfully performed forward() with an input of {px}")

def backward(px):
    t.backward(px)
    print(f"Successfully performed backward() with an input of {px}")

def penup(val):
    if val:
        t.penup
        mPen = "penup"
    elif not val:
        t.pendown
        mPen = "pendown"
    print(f"Successfully performed penup() with an input of {mPen}")

def circle(rad):
    t.circle(rad)
    print(f"Successfully performed circle() with an input of {rad}")

def square(len):
    # loop 1
    t.right(90)
    t.forward(len)
    # loop 2
    t.right(90)
    t.forward(len)
    # loop 3
    t.right(90)
    t.forward(len)
    # loop 4
    t.right(90)
    t.forward(len)
    print(f"Successfully performed square() with an input of {len}")

def hexagon(len):
    # loop 1
    t.right(60)
    t.forward(len)
    # loop 2
    t.right(60)
    t.forward(len)
    # loop 3
    t.right(60)
    t.forward(len)
    # loop 4
    t.right(60)
    t.forward(len)
    # loop 5
    t.right(60)
    t.forward(len)
    # loop 6
    t.right(60)
    t.forward(len)
    print(f"Successfully performed hexagon() with an input of {len}")