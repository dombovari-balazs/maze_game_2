import string

def buildEmptyMap(columns, rows):
    mapMatrix= [[0 for x in range(columns)] for x in range(rows)]
    return mapMatrix


def print_map(mapMatrix):
    print("You've opened: print_map(mapMatrix)")
    print("Funct: print_map()")
    for line in mapMatrix:
        print(line)


def print_map2(mapMatrix, rows):
    print("You've opened: print_map2(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            print(mapMatrix[y][x], end='')
    print()






def format_map_excel(mapMatrix, rows):
    print("You've opened: format_map_excel(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            if mapMatrix[y][x] == '\t':
               mapMatrix[y][x] = ''
            elif mapMatrix[y][x] == '\n':
                pass
            
            else:
                print(mapMatrix[y][x], end='')
        print()
    return mapMatrix



def format_map_every2nd(mapMatrix, rows):
    print("You've opened: format_map_every2nd(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            if x%2 == 0:
                if mapMatrix[y][x] == '\t':
                    mapMatrix[y][x] = ''
            elif mapMatrix[y][x] == '\n':
                mapMatrix[y][x] = ' '
            
            else:
                print(mapMatrix[y][x], end='')
        print()
    return mapMatrix


def format_map_0finder(mapMatrix, rows):
    print("You've opened: format_map_0finder(mapMatrix, rows)")
    for y in range(rows):
        for x in range(len(mapMatrix[y])):
            if mapMatrix[y][x] == '0':
                mapMatrix[y][x] = ' '
    return mapMatrix


def openTroll():
    with open('cicaTrollFace.txt', 'r' ) as mazeFileTroll:
        columns = 57
        rows = 58
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileTroll:
            mapKacsa[i] = list(line)
            i += 1
        
        basic_dictonary = {
            'positionStartYX' : [5,3], #TODO
            'positionFinal' :[34,45],
            'map' : mapKacsa,
        }
        print_map2(mapKacsa, rows)
        #return basic_dictonary



def openTest():
    with open('mazeFileLvl_test.txt', 'r' ) as mazeFileLvl_test:
        columns = 10
        rows = 10
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileLvl_test:
            mapKacsa[i] = list(line)
            i += 1
        format_map_excel(mapKacsa,rows)
        format_map_0finder(mapKacsa,rows)

        basic_dictonary = {
            'positionStartYX' : [5,3], #TODO
            'positionFinal' :[34,45],
            'map' : mapKacsa,
        }
        return basic_dictonary
        
        


def open1():
    with open('mazeFileLvl_1.txt', 'r' ) as mazeFileLvl_1:
        columns = 11
        rows = 11
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileLvl_1:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1

        basic_dictonary = {
            'positionStartYX' : [5,3], #TODO
            'positionFinal' :[34,45],
            'map' : mapKacsa,
        }
        return basic_dictonary

######################################################################


def open_hexa():
    with open('mazeFileLvl_hexa.txt', 'r' ) as mazeFileLvl_hexa:
        columns = 59
        rows = 30
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileLvl_hexa:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1
        
        basic_dictonary = {
            'positionStartYX' : [5,3], #TODO
            'positionFinal' :[34,45],
            'map' : mapKacsa,
        }
        print_map2(mapKacsa, rows)
        #return basic_dictonary

######################################################################


def open_bunny():
    with open('mazeFileLvl_Bunny.txt', 'r' ) as mazeFileLvl_Bunny:
        columns = 67
        rows = 39
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in mazeFileLvl_Bunny:
            mapKacsa[i] = list(line)
            #print(list(line))
            i += 1
        
        basic_dictonary = {
            'positionStartYX' : [5,3], #TODO
            'positionFinal' :[34,45],
            'map' : mapKacsa,
        }
        #return basic_dictonary
        print_map2(mapKacsa,rows)


def open_screenFinal():
    with open('screenFinal', 'r' ) as fileScreenFinal:
        columns = 67
        rows = 34
        mapKacsa = buildEmptyMap(columns,rows)
        i = 0
        for line in fileScreenFinal:
            mapKacsa[i] = list(line)
            i += 1
        
        basic_dictonary = {
            'positionStartYX' : [5,3], #TODO
            'positionFinal' :[34,45],
            'map' : mapKacsa,
        }
        return basic_dictonary

def simoMosogassEl():
    mapTroll = openTroll()
    mapTest = openTest()
    map1 = open1()
    mapHexa = open_hexa()
    mapBunny = open_bunny()
    mapFinal = open_screenFinal()

#openTroll()
#open_hexa()
#open_bunny()