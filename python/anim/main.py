# startup
import animator as anim
import os

global mainLoop
global lineNum
global data
mainLoop = True
lineNum = 1
data = []

print("|=======================================|")
print("|     Hello, welcome to pyAnimator!     |")
print("|                                       |")
print("|           CHANGELOG 0.0.1:            |")
print("|           - Made it work              |")
print("|           - Added rCircle             |")
print("|           - Added pat(tern)           |")
print("|           - Added speed               |")
print("|           - Added display             |")
print("|=======================================|")

# clearing the screen
print("")
print("Press enter to begin")
input() 
os.system('cls' if os.name == 'nt' else 'clear')

# main code
while mainLoop:
    inp = input(f"{lineNum}: ")

    if inp == "exit":
        print("Bye!")
        exit()

    if inp == "compile":
        mainLoop = False
    
    if not inp == "exit" and not inp == "compile":
        lineNum += 1
    
    if not inp == "exit" and not inp == "compile":
        data.append(inp)

print(data[1])