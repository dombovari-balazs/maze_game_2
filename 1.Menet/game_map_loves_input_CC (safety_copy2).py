# Taskok
    # Nagyobb map
    # A palya szele az univerzalis '#' legyen
    # globalis valtozok off
    # fuggveny rendszer megszervezese

import os
import time

objectWall = 'x'
objectEmpty = '.'
objectPlayer = '@'

# Empty map maker
def mapMaker():
    mapMatrixExample = [[0 for x in range(5)] for x in range(5)]
    return mapMatrixExample

# read the map
def map_loader(mapMatrix):
    mapGiven = [
    "xxxxx",
    "x...x",
    "x.o.x",
    "x...x",
    "xxxxx"
    ]

    mapMatrixNew = mapMatrix
    for y in range(len(mapMatrix)):
        mapMatrixNew[y] = list(mapGiven[y])
    #print_map(mapMatrixNew)
    return mapMatrixNew

# We can print the map as well :3
def print_map(mapMatrix):
    for y in range(len(mapMatrix)):
        for x in range(len(mapMatrix[y])):
            print(mapMatrix[y][x], end='')
        print()


def printMenu():
    print("Hi! Welcome in my game! :3")
    print("(1)  Play")
    print("(2)  Options")
    print("(3)  About the Game")
    print("(0)  Exit")

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# Beallitjuk, hogy hova dobja le a kis karakterunket


def startGame(mapMatrixPlay, pos_y, pos_x, speed):
    playing = True
    while playing:
        #print("The new position is: ", position_YX_O)

        print_map(mapMatrixPlay)
        userInput = getch()

        if userInput == 'w':
            if mapMatrixPlay[pos_y - speed][pos_x] == objectWall:
                pass
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                
                pos_y -= speed
            # Ez csak ugy itt maradt
            # pos_y_new =  pos_y - speed
            

        elif userInput == 's':
            #pos_y_new =  pos_y + speed
            if mapMatrixPlay[pos_y + speed][pos_x] == objectWall:
                pass
            
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                
                pos_y += speed

        elif userInput == 'd':
            #pos_x_new = pos_x + speed
            if mapMatrixPlay[pos_y][pos_x + speed] == objectWall:
                pass
            
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                
                pos_x += speed

        elif userInput == 'a':
            #pos_x_new = pos_x_new - speed
            if mapMatrixPlay[pos_y][pos_x - speed] == objectWall:
                pass
            
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                
                pos_x -= speed

        elif userInput == 'p':
            playing = False
        
        else:
            print("That wasn't a correct input, try again!")
            time.sleep(0.2)
            os.system('clear')
            continue 
        
        
        position_YX_O = [pos_y, pos_x]
        mapMatrixPlay[pos_y][pos_x] = objectPlayer # ahova megyek azt playerre csinalom
        mapMatrixPlay[pos_old_y][pos_old_x] = objectEmpty # megjegyeztem, hogy honnan megyek, oda palya elemet rakok
        
        
        os.system('clear')
        
        print("The new position is: ", position_YX_O)

def menuNotReady(menuOption):
    os.system('clear')
    print(menuOption)
    print()
    print("Sorry, this option is not yet ready for use :( ")
    print("Press any button to continue :) ")
    getch()
    


def main():
    os.system('clear')

    # Palyaepites
    mapMatrixExample = mapMaker()
    mapMatrixPlay = map_loader(mapMatrixExample)
    
    # Beallitasok
    pos_y = 2
    pos_x = 2
    speed = 1
    
    #Itt legyen a menu
    game = True
    while game:
        os.system('clear')
        printMenu()
        userMenuInput = getch()

        if userMenuInput == '1': # Play
            os.system('clear')
            startGame(mapMatrixPlay, pos_y, pos_x, speed)
        
        elif userMenuInput == '2': # Settings
            menuNotReady("Settings")
            
        
        elif userMenuInput == '3': # About the game
            menuNotReady("About the game")

        elif userMenuInput == '0': 
            game = False
        else:
            os.system('clear')
            print("Sorry, that wasn't an option..."," You pressed", userMenuInput )

            print("Press any button to continue :) ")
            getch()
            
if __name__ == "__main__" :
    main()
