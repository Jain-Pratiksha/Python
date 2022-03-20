# EXP 7: Colour Map Problem
# Name: Pratiksha Jain


# To create region with name and color
class region:
    def __init__(self, rName, rColor):
        self.rName = rName  # region name
        self.rColor = rColor  # region color
        self.adjecentRegions = []  # list to store objects of Adjacent region

    def setAdjacentR(self, adjecentRegions):
        self.adjecentRegions = adjecentRegions  # set objects no. Adjacent regions


# print colors of all regions
def printState():
    print("Region 1 color: ", R1.rColor)
    print("Region 2 color: ", R2.rColor)
    print("Region 3 color: ", R3.rColor)
    print("Region 4 color: ", R4.rColor)
    print("Region 5 color: ", R5.rColor)
    print("Region 6 color: ", R6.rColor)
    print("Region 7 color: ", R7.rColor)
    print("Region 8 color: ", R8.rColor)


# valivate colour entered by user
def validateInput(color):
    # color list
    colors = ['R', 'G', 'Y', 'B']
    # check if user color input is in list of required colors
    if color in colors:
        return True
    else:
        print("Invalid color input")
        return False

    # validate user input color with Adjacent region colors


def validateColor(region, color):
    # get list of colors of all adjecent regions
    colors_of_Adjacent_r = [region.rColor for region in region.adjecentRegions]
    # check if user input color is present in list of Adjacent region color
    if color in colors_of_Adjacent_r:
        print("one of the Adjacent region has same color!!")
        print("!!!!! GAME OVER !!!!!")
        return False
    else:
        return True


# if user lost the game clear colors set by him. by painting all regions with default white color
def clearMemory():
    R1.rColor = 'white'
    R2.rColor = 'white'
    R3.rColor = 'white'
    R4.rColor = 'white'
    R5.rColor = 'white'
    R6.rColor = 'white'
    R7.rColor = 'white'
    R8.rColor = 'white'


# DRIVER CODE

# number of regions
N = 8

# object of regions
# Initially lets paint all regions with white color
R1 = region('R1', 'White')
R2 = region('R2', 'White')
R3 = region('R3', 'White')
R4 = region('R4', 'White')
R5 = region('R5', 'White')
R6 = region('R6', 'White')
R7 = region('R7', 'White')
R8 = region('R8', 'White')

# set adjacent regions all regions by passing list of Adjacent regions object
R1.setAdjacentR([R2, R5, R6, R4])
R2.setAdjacentR([R1, R5, R8, R3])
R3.setAdjacentR([R2, R8, R7, R4])
R4.setAdjacentR([R1, R6, R7, R3])
R5.setAdjacentR([R1, R2, R6, R8])
R6.setAdjacentR([R1, R4, R5, R7])
R7.setAdjacentR([R4, R3, R6, R8])
R8.setAdjacentR([R3, R2, R7, R5])

while (True):
    print("===================NEW GAME==================")
    print("R,G,Y,B")
    c1 = input("Enter color for region 1: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c1)):
        # color region with color entered by user
        R1.rColor = c1
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c2 = input("Enter color for region 2: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c2) and validateColor(R2, c2)):
        # color region with color entered by user
        R2.rColor = c2
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c3 = input("Enter color for region 3: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c3) and validateColor(R3, c3)):
        # color region with color entered by user
        R3.rColor = c3
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c4 = input("Enter color for region 4: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c4) and validateColor(R4, c4)):
        # color region with color entered by user
        R4.rColor = c4
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c5 = input("Enter color for region 5: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c5) and validateColor(R5, c5)):
        # color region with color entered by user
        R5.rColor = c5
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c6 = input("Enter color for region 6: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c6) and validateColor(R6, c6)):
        # color region with color entered by user
        R6.rColor = c6
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c7 = input("Enter color for region 7: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c7) and validateColor(R7, c7)):
        # color region with color entered by user
        R7.rColor = c7
        # print current state
        printState()
    else:
        # paint all regions with white again and start new game
        clearMemory()
        continue

    print("============================================")
    c8 = input("Enter color for region 8: ")
    # validate color entered by user. here we dont need to validate color wrt to color of adjecent regions.
    if (validateInput(c8) and validateColor(R8, c8)):
        # color region with color entered by user
        R8.rColor = c8
        # print current state
        printState()
        # as all regions are painted by satisfying all condition goal is achieved
        print("You won the game!")
        # paint all regions with white again and start new game
        clearMemory()
        break
    else:
        # print all regions with white again and start new game
        clearMemory()
        continue



