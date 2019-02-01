# Ok. Rage. Nem talaltam az interneten rendes ASCII map generatort/makert/editort
# Ugyhogy most irok egyet magamnak.


import os
import time
import glob

# Empty map maker
def mapMaker(mapFileLen):
    mapMatrixExample = [['0' for x in range(mapFileLen)] for x in range(mapFileLen)]
    return mapMatrixExample


def mapMaker_byUserInput(size):
    mapMatrixExample = [['.' for x in range(size)] for x in range(size)]
    return mapMatrixExample


# read the map
def map_loader(mapMatrix):
    mapGiven = [
    "#####",
    "#...#",
    "#.@.#",
    "#...#",
    "#####"
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
    print("(4)  Open Map editor")
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

def printInfo(position_YX_O):
    print()
    print("The current position is: ", position_YX_O)
    print("You can move with 'W' 'A' 'S' 'D', and you can go back to the menu with 'P' ")


def startGame(mapMatrixPlay, pos_y, pos_x, speed, objectWall, objectEmpty, objectPlayer):
    playing = True
    position_YX_O = [pos_y, pos_x]
    while playing:
        
        print_map(mapMatrixPlay)

        printInfo(position_YX_O)    
        
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
        

def changeMode():
    print("You have planty of choise: \n (1):'#' is wall object. \n (2):'.' is empty object. \n (3):'O' is door object.")
    print(" (4): '~' is see object. \n (5): 'c' is coin object. \n (6): ' ' is nothing object. ")
    print(" (7): If you want to only move")
    userModeInput = getch()
    if userModeInput == '1':
        return '#'
    if userModeInput == '2':
        return '.'
    if userModeInput == '3':
        return 'O'
    if userModeInput == '4':
        return '~'
    if userModeInput == '5':
        return 'c'
    if userModeInput == '6':
        return ' '
    
    if userModeInput == '7':
        return 'basic'
    
    else:
        print("Sorry I can't deal with this information.")
        return  '.'

def loadFromFile():
    print("Eppen fajlbol toltunk be.")

    # Printing Folder content
    folderContent = glob.glob("/home/dombalazs/codecool/PetProject/mazeGame_2_0/2.Menet/*.txt")
    for content in folderContent:
        print(content)
    print("")
    userInputFileName = input("Please Choose a file: ")

    with open(userInputFileName, 'r') as mapFile:
        # Egy ciklussal vegignezzuk a fajlt. Kimentve a hosszat.
        mapFileLen = 0
        for line in mapFile:
            mapFileLen += 1
        
        # Letrehozunk egy ures matrixot, amibe majd tudunk irni
        mapMatrix = mapMaker(mapFileLen)

        #print(mapFileLen)
        i = 0
        #time.sleep(3)

        # feltoltjuk az adattal a matrixot
        print("Most a for loop elott vagyunk.")

        # vissza kell ugrani az elejere
        mapFile.seek(0)
        for line in mapFile:
            mapMatrix[i] = list(line)
            print(mapMatrix[i])
            i += 1
        for line in range(len(mapMatrix)):
            mapMatrix[line].remove('\n')
        print("Most a for loop utan vagyunk.")
        #time.sleep(3)
        # format_map_excel(mapKacsa,rows)
        # format_map_0finder(mapKacsa,rows)
        return mapMatrix
    

def saveToFile(mapMatrix):
    userInputMapname = input("Write your map name: ")
    with open(userInputMapname, 'w') as mapFile:
        for line in range(len(mapMatrix)):
            for character in range(len(mapMatrix[line])):
                mapFile.write(mapMatrix[line][character])
            mapFile.write('\n')
    
    


    
def openMapEditor(mapMatrixPlay, pos_y, pos_x, speed, objectWall, objectMode, objectPlayer, size):
    # Ask the user for the parameters 
        # meretek: Hanyszor hanyas
        # Legyen-e szele
    
    # Generaljuk le a kert palyat, a bal felso sarokba helyezzuk el a karaktert

    # Legyenek modok, hogy mit rakjon utanunk, amikor mozgunk.

    # Alulra irja ki a helyzetet: 
        # Hol vagyunk
        # Milyen modban vagyunk
        # instrukciok
    os.system('clear')
    playing = True
    position_YX_O = [pos_y, pos_x]
    
    objectModeEditor = '.'

    # Ez azert kell, hogy kesobb tudjam valtoztatni
    objectModeEditor = objectMode
    
    while playing:
        
        print_map(mapMatrixPlay)

        printInfo(position_YX_O)    
        
        userInput = getch()

        
        if userInput == 'w':
            if pos_y - speed < 0:
                pass
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                objectBehind = mapMatrixPlay[pos_y - speed][pos_x]
                    
                #pos_next_x = pos_x
                #pos_next_y = pos_y - speed
                
                pos_y -= speed
            # Ez csak ugy itt maradt
            # pos_y_new =  pos_y - speed
            

        elif userInput == 's':
            #pos_y_new =  pos_y + speed
            if pos_y + speed > size - 1:
                pass
            
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                objectBehind = mapMatrixPlay[pos_y + speed][pos_x]
                
                #pos_next_x = pos_x
                #pos_next_y = pos_y + speed

                pos_y += speed

        elif userInput == 'd':
            #pos_x_new = pos_x + speed
            if pos_x + speed > size - 1:
                pass
            
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                objectBehind = mapMatrixPlay[pos_y][pos_x + speed]
                
                #pos_next_x = pos_x + speed
                #pos_next_y = pos_y 
                
                pos_x += speed

        elif userInput == 'a':
            #pos_x_new = pos_x_new - speed
            if pos_x - speed  < 0:
                pass
            
            else:
                pos_old_x = pos_x
                pos_old_y = pos_y
                
                objectBehind = mapMatrixPlay[pos_y][pos_x - speed]
                #pos_next_x = pos_x - speed
                #pos_next_y = pos_y 
                
                pos_x -= speed

        elif userInput == 'p':
            print("Do you want to save this map?")
            print("If yes press (1)")
            print("If no press  (2)")
            userInputSave = getch()
            if userInputSave == '1':
                saveToFile(mapMatrixPlay)

            playing = False

        
        elif userInput == 'm':
            objectModeEditor = changeMode()
            print("Mar lefutott a fuggveny, az uj mode ", objectModeEditor)
            
        else:
            print("That wasn't a correct input, try again!")
            time.sleep(0.2)
            os.system('clear')
            continue 
        
        
        position_YX_O = [pos_y, pos_x]
        mapMatrixPlay[pos_y][pos_x] = objectPlayer # ahova megyek azt playerre csinalom
        
        
        if objectModeEditor == 'basic':
            
            #mapMatrixPlay[pos_old_y][pos_old_x] = objectBehind    
            mapMatrixPlay[pos_y][pos_x] = objectBehind    
        
        else:
            mapMatrixPlay[pos_old_y][pos_old_x] = objectModeEditor # megjegyeztem, hogy honnan megyek, oda palya elemet rakok
        
        
        os.system('clear')

    
    pass
    

def menu(mapMatrixPlay, pos_y, pos_x, speed, objectWall, objectEmpty, objectPlayer):
    game = True
    while game:
        os.system('clear')
        printMenu()
        userMenuInput = getch()
        if userMenuInput == '1': # Play
            os.system('clear')
            startGame(mapMatrixPlay, pos_y, pos_x, speed, objectWall, objectEmpty, objectPlayer)
        
        elif userMenuInput == '2': # Settings
            menuNotReady("Settings")
            
        
        elif userMenuInput == '3': # About the game
            menuNotReady("About the game")

        elif userMenuInput == '4': # Open map editor
            
            userEditorInput = int(input("Give me a size between 5 and 50: "))
            # TODO itt ki tud akadni a program #BUG
            mapMatrixEditor = mapMaker_byUserInput(userEditorInput)
            openMapEditor(mapMatrixEditor, pos_y, pos_x, speed, objectWall, objectEmpty, objectPlayer, userEditorInput)

        elif userMenuInput == '0': 
            game = False
        else:
            os.system('clear')
            print("Sorry, that wasn't an option..."," You pressed", userMenuInput )

            print("Press any button to continue :) ")
            getch()
    


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
    #mapMatrixExample = mapMaker()
    #mapMatrixPlay = map_loader(mapMatrixExample)
    mapMatrixPlay = loadFromFile()

    # Beallitasok
    pos_y = 2
    pos_x = 2
    speed = 1
    objectWall = '#'
    objectEmpty = '.'
    objectPlayer = '@'

    
    #Itt legyen a menu
    menu(mapMatrixPlay, pos_y, pos_x, speed, objectWall, objectEmpty, objectPlayer)
            
if __name__ == "__main__" :
    main()


# Tovabbi dolgok:
    # Tudjon fajlba menteni
    # Tudjon specifikus karaktereket lerakni, amit a user ad meg.
    # Tudjon koordinatara ugrani
