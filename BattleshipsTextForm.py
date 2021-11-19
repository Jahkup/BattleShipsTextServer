############BATTLESHIPS###########

###NOTES:
#Make functions for terms and every avaliable move
#connect game to server
#develop method for allowing enemy to make a turn (work on alllowing the enemy to make a move on the same computer first?)

##CLASSES

class CELL:
    def __init__(self, id, hit, shipquater):
        self.ID = id #string
        self.HIT = hit #bool
        self.SHIPQ = shipquater #bool

    def __str__(self):
        return self.ID

class Boat:
    def __init__(self):
        self.boatFive = True
        self.boatFour = True
        self.boatThree = True
        self.boatTwo = True
        self.boatOne = True


##FUNCTIONS

def setup_your_boats(board):
    boats = Boat()
    while not boats.boatOne and not boats.boatTwo and not boats.boatThree and not boats.boatFour and not boats.boatFive: #will keep running till there are no more selectable boats
        print("Possible boats to play:")
        if boats.boatFive:
            print("Long Boat (5 Long)")
        if boats.boatFour:
            print("General Boat (4 Long)")
        if boats.boatThree:
            print("Medium Boat (3 Long)")
        if boats.boatTwo:
            print("Small Boat (2 Long)")
        if boats.boatOne:
            print("Spy Boat (1 Long)")

        selected_boat = input("Please select the length of the boat. (1-5): ").strip()
        if selected_boat == "":
            print("Please enter a valid number")
            continue

        try:
            selected_boat = int(selected_boat)
        except ValueError:
            print("Please enter a number")
            continue

        if selected_boat > 5 or selected_boat < 1:
            print("Please enter a valid length.")
            continue

        if selected_boat == 1 and not boats.boatOne:
            print("Spy boat has been placed already.")
            continue
        if selected_boat == 2 and not boats.boatTwo:
            print("Small boat has been placed already.")
            continue
        if selected_boat == 3 and not boats.boatThree:
            print("Medium boat has been placed already.")
            continue
        if selected_boat == 4 and not boats.boatFour:
            print("General boat has been placed already.")
            continue
        if selected_boat == 5 and not boats.boatFive:
            print("Large boat has been placed already.")
            continue
        ###THE LENGTH OF BOAT SUCCESSFULLY VALIDATED

        while True: #Get the angle
            print("Would you like the boat Horizontal or Vertical.")
            hor_ver = input("H or V: ").lower().strip()
            if hor_ver == "":
                print("Please enter something")
                continue
            if hor_ver != "v" or hor_ver != "h":
                print("Please enter a valid input.")
                continue
            break
        ##The Angle Has Been Validated

        acceptedChars = "ABCDEFGH"
        while True:
            print("where do you want the head of the boat? (top to bottom, left to right)")
            placement = input("Input Grid #: ").strip().upper()
            if placement == "":
                print("Please enter something")
                continue
            try:
                placementNumber = int(placement[0])
            except ValueError:
                print("Please enter a digit for the first reference number")
                continue
            if placement[1] not in acceptedChars:
                print("please enter a valid grid letter.")
                continue
            if len(placement) > 2 or len(placement) < 1:
                print("please enter a valid grid #")
                continue
            #grid # is valid, check if end of boat fits
            if hor_ver == "H":
                checker = ord(placement[1])
                if (checker+selected_boat) > 72:
                    print("The length of the boat goes off the grid, try again.")
                    continue
            else:
                if (placementNumber+selected_boat) > 8:
                    print("The length of the boat goes off the grid, try again.")
                    continue
            if placement[1] == "A":
                ETUP = str(placementNumber)+"1"
            elif placement[1] == "B":
                ETUP = str(placementNumber)+"2"
            elif placement[1] == "C":
                ETUP = str(placementNumber) + "2"
            elif placement[1] == "D":
                ETUP = str(placementNumber)+"2"
            elif placement[1] == "E":
                ETUP = str(placementNumber)+"2"
            elif placement[1] == "F":
                ETUP = str(placementNumber)+"2"
            elif placement[1] == "G":
                ETUP = str(placementNumber)+"2"










def get_enemy_board_boats(board):
    #get direct grid array from server enemyside
    pass

def make_your_move():
    pass

def hit_or_miss():  #i guess you never miss huh? you got a boyfriend, i bet he doesnt kiss ya!
    pass

def connect_to_server():
    pass

def win_or_lose():
    pass

def display_grid(board):
    pass

def wait_for_responce():
    pass

rws = 8
cls = "ABCDEFGH"
rows = []
cols = []
for R in range(1,rws+1):
    cols = []
    for C in cls:
        cols.append(CELL((str(R)+str(C)), False, False))
    rows.append(cols) #The setup would end up like [[1A, 1B, 1C, 1D], [2A, 2B, 2C, 2D], [3A, 3B, 3C, 3D], [4A, 4B, 4C, 4D]]. ( [rows[column]]

your_board = rows #This will be an empty grid
enemy_board = rows #This will be an empty grid

setup_your_boats(your_board)





