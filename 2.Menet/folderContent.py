import os

#print(os.path('/home/dombalazs/codecool/PetProject/mazeGame_2_0'))
import glob
folderContent = glob.glob("/home/dombalazs/codecool/PetProject/mazeGame_2_0/2.Menet/*.txt")
for content in folderContent:
    print(content)