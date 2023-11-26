# startup
import animator as anim
import os

global cDebug
global mainLoop
global lineNum
global data
global sDoc
sDoc = False
mainLoop = True
lineNum = 0
data = []
version = "0.0.1"
cDebug = True

print(f"|=======================================|")
print(f"|     Hello, welcome to pyAnimator!     |")
print(f"|                                       |")
print(f"|           CHANGELOG {version}:        |")
print(f"|           - Made it work              |")
print(f"|           - Added rCircle             |")
print(f"|           - Added pat(tern)           |")
print(f"|           - Added speed               |")
print(f"|           - Added display             |")
print(f"|=======================================|")

# clearing the screen
ini = input("Action: ") 
os.system('cls' if os.name == 'nt' else 'clear')

if ini == "docs":
    sDoc = True

while sDoc:
    docIndex = input("code to search: ")
    
    if docIndex == "rCircle":
        print("")
        print("rCircle")
        print("Creates a circle and adds the radius of it to the center")
        print("")
        print("CODE: rCircle(p1,p2,p3)")
        print("")
        print("p1: radius of given circle")
        print("p2: fontsize of text (radius)")
        print("p3: spacing between circle and text (p2)")
        print("")
        print("Reads 3 digits of each parameter")
        print("")
        print("EXAMPLE:")
        print("rCircle(150,016,010)")
        print("")

        cont = input("Search again? ")
        if cont == "yes":
            sDoc = True
        else:
            sDoc = False

    if docIndex == "exit":
        sDoc = False

# Start Screen

print("")
print("Press enter to begin")
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
        cDebug = False
        param1 = cRun[8] + cRun[9] + cRun[10]
        param2 = cRun[12] + cRun[13] + cRun[14]
        param3 = cRun[16] + cRun[17] + cRun[18]
        p1 = int(param1)
        p2 = int(param2)
        p3 = int(param3)
        anim.rCircle(p1, p2, p3)

    if "pat" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # pat(par1,par2)
        param1 = cRun[5] + cRun[6] + cRun[7]
        param2 = cRun[9] + cRun[10] + cRun[11] + cRun[12]
        p1 = int(param1)
        p2 = int(param2)
        anim.pat(p1, p2)

    if "speed" in cRun:
        print(f"Running command: {cRun}")
        cDebug = False # speed(10)
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

    if cDebug:
        print(f"")
        print(f"Fatal error on line: {cRepeat}")
        print(f"Whilst Running code: {cRun}")
        print(f"Exiting program")
        exit()

    cRepeat += 1
