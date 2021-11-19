import tkinter as tk
###NOTES
#show whos turn it is
#OPTIONAL: Sounds
#determine how a winner and loser is found

class CELL:
    def __init__(self, id, hit, shipquater):
        self.ID = id #string
        self.HIT = hit #bool
        self.SHIPQ = shipquater #bool

    def __str__(self):
        return self.ID

class butn:
    def __init__(self, id, clicked, colour, rw, cl):
        self.buttonNumber = id
        self.clikd = clicked
        self.colour = colour
        self.RW = rw
        self.CL = cl



class you_hit:
    #this will show everything you have hit or attempted to hit
    def __init__(self, cells):
        self.Cells = cells #the array of an array
    pass

class your_board:
    #this will show where your ships are and where the opponent has hit you
    def __init__(self, cells):
        self.Cells = cells #the array of an array
    pass


def buttonClick(rowN, colN):
    print(rowN,colN)



##INIT THE CELLS
rws = 8
cls = 8
rows = []
cols = []
for R in range(1,rws+1):
    cols = []
    for C in range(1,cls+1):
        cols.append(CELL((str(R)+str(C)), False, False))
    rows.append(cols)

yourBoard = your_board(rows) #an empty array of a grid and cells
yourHitScreen = you_hit(rows) #an empty array of a grid and cells


for row in yourBoard.Cells:
    for col in row:
        print(col, end=" ")
    print("\n")

window = tk.Tk()

gridarea = window.grid()

label = tk.Label(master=window, text="Enemy Side").grid(row=0,column=3,columnspan=2)

for R in range(1,rws+1):
    for C in range(cls):
        button = tk.Button(
            master=gridarea,
            text="",
            width=6,
            height=3,
            bg="lightgray",
            fg="yellow",
            command=buttonClick(R,C)
        )
        button.grid(row=R, column=C)
        button.pack

label = tk.Label(master=window, text="Your Side", pady=5).grid(row=rws+1,column=3,columnspan=2,sticky="s")

for R in range(10,rws+(rws+2)):
    for C in range(cls):
        button = tk.Button(
            text="",
            width=6,
            height=3,
            bg="lightgray",
            fg="yellow",
        )
        button.grid(row=R, column=C)













window.mainloop()
