# startup
import animator as anim
import os

global cDebug
global mainLoop
global lineNum
global data
mainLoop = True
lineNum = 0
data = []
version = "0.0.1"
cDebug = True

print(f"|=======================================|")
print(f"|     Hello, welcome to pyAnimator!     |")
print(f"|                                       |")
print(f"|           CHANGELOG {version}:            |")
print(f"|           - Made it work              |")
print(f"|           - Added rCircle             |")
print(f"|           - Added pat(tern)           |")
print(f"|           - Added speed               |")
print(f"|           - Added display             |")
print(f"|=======================================|")

# clearing the screen
print("Press enter to begin")
input("")
os.system('cls' if os.name == 'nt' else 'clear')

# main code
while mainLoop:
    inp = input(f"{lineNum}: ")

    if inp == "exit":
        print("Bye!")
        exit()

    if inp == "comp":
        mainLoop = False
    
    if not inp == "exit" and not inp == "compile":
        lineNum += 1
    
    if not inp == "exit" and not inp == "comp":
        data.append(inp)

# running code
datLen = len(data)

print(f"")
print(f"Compiling...")
print(f"Total lines: {datLen}")
print(f"")

cRepeat = 0
while not cRepeat == datLen:
    print(f"Running line: {cRepeat}")
    cRun = data[cRepeat]
    cDebug = True

    if "rCircle" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # rCircle(xxxx,xxx,xxx)
        param1 = cRun[8] + cRun[9] + cRun[10] + cRun[11]
        param2 = cRun[12] + cRun[13] + cRun[14]
        param3 = cRun[16] + cRun[17] + cRun[18]
        p1 = int(param1)
        p2 = int(param2)
        p3 = int(param3)
        anim.rCircle(p1, p2, p3)

    if "pat" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # pat(xxx,xxxx)
        param1 = cRun[4] + cRun[5] + cRun[6]
        param2 = cRun[8] + cRun[9] + cRun[10] + cRun[11]
        p1 = int(param1)
        p2 = int(param2)
        anim.pat(p1, p2)

    if "speed" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # speed(xx)
        param1 = cRun[6] + cRun[7]
        p1 = int(param1)
        anim.speed(p1)

    if "display" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False
        if "True" in cRun:
            anim.display(True)
        if "False" in cRun:
            anim.display(False)

    if "left" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # left(xxx)
        param1 = cRun[5] + cRun[6] + cRun[7]
        p1 = float(param1)
        anim.left(p1)

    if "right" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # right(xxx)
        param1 = cRun[6] + cRun[7] + cRun[8]
        p1 = float(param1)
        anim.right(p1)

    if "forward" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # forward(xxxx)
        param1 = cRun[8] + cRun[9] + cRun[10] + cRun[11]
        p1 = float(param1)
        anim.forward(p1)

    if "backward" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # backward(xxxx)
        param1 = cRun[9] + cRun[10] + cRun[11] + cRun[12]
        p1 = float(param1)
        anim.backward(p1)

    if "penup" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False
        anim.penup(True)

    if "pendown" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False
        anim.penup(False)

    if "circle" in cRun and not "rCircle" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # circle(xxxx)
        param1 = cRun[7] + cRun[8] + cRun[9] + cRun[10]
        p1 = int(param1)
        anim.circle(p1)

    if "square" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # square(xxxx)
        param1 = cRun[7] + cRun[8] + cRun[9] + cRun[10]
        p1 = int(param1)
        anim.square(p1)

    if "hexagon" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # hexagon(xxxx)
        param1 = cRun[8] + cRun[9] + cRun[10] + cRun[11]
        p1 = int(param1)
        anim.hexagon(p1)

    if cDebug:
        print(f"")
        print(f"Fatal error on line: {cRepeat}")
        print(f"Whilst Running code: {cRun}")
        print(f"Exiting program")
        exit()

    cRepeat += 1