map1 = [
    "xxxxx",
    "x...x",
    "x.o.x",
    "x...x",
    "xxxxx"
]
# Empty map maker
mapMatrixExample = [[0 for x in range(5)] for x in range(5)]


# read the map
def map_reader(mapMatrix, mapGiven):
    mapMatrixNew = mapMatrix
    for y in range(len(mapMatrix)):
        mapMatrixNew[y] = list(mapGiven[y])
    print_map(mapMatrixNew)


def print_map(mapMatrix):
    for y in range(len(mapMatrix)):
        for x in range(len(mapMatrix[y])):
            print(mapMatrix[y][x], end='')
        print()



# lol
print("The map we just made: ")
print_map(mapMatrixExample)

print("The map, we read in: ")
map_reader(mapMatrixExample,map1)

# Let's figure it out, how can we move in the map




pos_y = 1
pos_x = 1
speed = 1
position_YX_O = [pos_y,pos_x]
print("The current position is: ", position_YX_O)
playing = True
while playing:
    userInput = input("What to do?")
    print("Your input was: ", userInput)
    if userInput == 'w':
        pos_y += speed
    elif userInput == 's':
        pos_y -= speed
    elif userInput == 'd':
        pos_x += speed
    elif userInput == 'a':
        pos_x -= speed
    elif userInput == 'p':
        playing = False
    else:
        print("That wasn't a correct input, try again!")
        continue 
    position_YX_O = [pos_y, pos_x]
    print("The new position is: ", position_YX_O)