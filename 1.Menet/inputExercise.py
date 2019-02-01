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



pos_y = 1
pos_x = 1
speed = 1
position_YX_O = [pos_y,pos_x]

playing = True
while playing:
    userInput = getch()
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
    elif userInput == '1':
        print("Mission succesful!")
    else:
        print("You pressed: ", userInput)
        print("That wasn't a correct input, try again!")
        continue 
    position_YX_O = [pos_y, pos_x]
    print("The new position is: ", position_YX_O)
