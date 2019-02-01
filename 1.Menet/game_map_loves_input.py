import os
os.system('clear')

# Ez a palyank, nagyon szeressuk.
map1 = [
    "xxxxx",
    "x...x",
    "x.o.x",
    "x...x",
    "xxxxx"
]

objectWall = 'x'
objectEmpty = '.'
objectPlayer = '@'

# Empty map maker
mapMatrixExample = [[0 for x in range(5)] for x in range(5)]


# read the map
def map_reader(mapMatrix, mapGiven):
    mapMatrixNew = mapMatrix
    for y in range(len(mapMatrix)):
        mapMatrixNew[y] = list(mapGiven[y])
    print_map(mapMatrixNew)
    return mapMatrixNew

# We can print the map as well :3
def print_map(mapMatrix):
    for y in range(len(mapMatrix)):
        for x in range(len(mapMatrix[y])):
            print(mapMatrix[y][x], end='')
        print()


# lol
print("The map we just made: ")
print_map(mapMatrixExample)

print("The map, we read in: ")
mapMatrixPlay = map_reader(mapMatrixExample,map1)

# Let's figure it out, how can we move in the map

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
pos_y = 2
pos_x = 2
speed = 1

# Ez csak tesztelesre kell, hogy hol van a kis karakterunk
position_YX_O = [pos_y,pos_x]

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
        continue 
    
    
    position_YX_O = [pos_y, pos_x]
    mapMatrixPlay[pos_y][pos_x] = objectPlayer # ahova megyek azt playerre csinalom
    mapMatrixPlay[pos_old_y][pos_old_x] = objectEmpty # megjegyeztem, hogy honnan megyek, oda palya elemet rakok
    
    
    os.system('clear')
    
    print("The new position is: ", position_YX_O)


# TODO: kipontozni 
    # Done
# TODO: megcsinálni a fal lekezelését
    # Ismert bug: Ha az elso lepesbol neki lehet menni a falnak, akkor meghal a program
    # Nincs kedvem most megoldani

# TODO: kommentezni

# Osszegzes: 
    # Mukszik a program.
    # Jok a kommentek
    # Nem CleanCode
        # Ehhez meg kellene oldani a fuggvenyeket
        # De beszedesek a valtozok, olvashato a kod.
        # vannak globalis valtozoim, sok... :D #global<3
    # kicsi a palya, de ugy van megcsinalva a program, hogy valtoztathato
    # kulon buszke vagyok a program eleji objectWall,objectPlayer, stb. definiciokra

# Kovi lepes
    # Nagyobb map
    # A palya szele az univerzalis '#' legyen
    # globalis valtozok off
    # fuggveny rendszer megszervezese
    