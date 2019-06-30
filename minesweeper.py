import random
from printcolorInTerminal import *

DIMENSION = 10

data = [[0 for i in range(DIMENSION)] for j in range(DIMENSION)]
play = [['◾' for i in range(DIMENSION)] for j in range(DIMENSION)]

def updateMines():
    i=0
    while i < DIMENSION:
        row = random.randint(0,6)
        col = random.randint(0,6)

        if data[row][col] != 9:
            data[row][col] = 9
            i+=1

def updateNumbers():
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            if data[row][col] != 9:
                continue
            else:
                if row > 0 and col > 0 and data[row-1][col-1] != 9: #top left
                    data[row-1][col-1] += 1
                if row > 0  and col < DIMENSION-1 and data[row-1][col+1] != 9: #top right
                    data[row-1][col+1] += 1
                if row > 0 and data[row-1][col] != 9: #top
                    data[row-1][col] += 1
                if col > 0 and data[row][col-1] != 9: #left
                    data[row][col-1] += 1
                if col < DIMENSION-1 and data[row][col+1] != 9: #right
                    data[row][col+1] += 1
                if row < DIMENSION-1 and data[row+1][col] != 9: #down
                    data[row+1][col] += 1
                if row < DIMENSION-1 and col > 0 and data[row+1][col-1] != 9: #down left
                    data[row+1][col-1] += 1
                if row < DIMENSION-1 and col < DIMENSION-1 and data[row+1][col+1] != 9: #down left
                    data[row+1][col+1] += 1


def actualDisplay():
    for rows in data:
        print(*rows)

def display():
    prYellow('   ' +'  '.join([str(i) for i in range(DIMENSION)]))
    print()
    i = 0
    for rows in play:
        prYellow(i)
        for cols in rows:
            if cols == '◾':
                prCyan(cols)
            else:
                prGreen(cols)
        i += 1
        print()

def reveal(row, col):
    if data[row][col] == 0:
        play[row][col] = '*'
        if row > 0 and col > 0: #top left
            if data[row-1][col-1] == 0:
                reveal(row-1, col-1)
            # elif data[row-1][col-1] != 9:
            #     play[row-1][col-1] = data[row-1][col-1]

        if row > 0  and col < DIMENSION-1: #top right
            if data[row-1][col+1] == 0:
                reveal(row-1, col+1)
            # elif data[row-1][col+1] != 9:
            #     play[row-1][col+1] = data[row-1][col+1]

        if row > 0: #top
            if data[row-1][col] == 0:
                reveal(row-1, col)
            # elif data[row-1][col] != 9:
            #     play[row-1][col] = data[row-1][col]

        if col > 0: #left
            if data[row][col-1] == 0:
                reveal(row, col-1)
            # elif data[row][col-1] != 9:
            #     play[row][col-1] = data[row][col-1]

        if col < DIMENSION-1: #right
            if data[row][col+1] == 0:
                reveal(row, col+1)
            # elif data[row][col+1] != 9:
            #     play[row][col+1] = data[row][col+1]

        if row < DIMENSION-1: #down
            if data[row+1][col] == 0:
                reveal(row+1, col)
            # elif data[row+1][col] != 9:
            #     play[row+1][col] = data[row+1][col]

        if row < DIMENSION-1 and col > 0: #down left
            if data[row+1][col-1] == 0:
                reveal(row+1, col-1)
            # elif data[row+1][col-1] != 9:
            #     play[row+1][col-1] = data[row+1][col-1]

        if row < DIMENSION-1 and col < DIMENSION-1: #down left
            if data[row+1][col+1] == 0:
                reveal(row+1, col+1)
            # elif data[row+1][col+1] != 9:
            #     play[row+1][col+1] = data[row+1][col+1]
            
    elif data[row][col] != 9:
        play[row][col] = data[row][col]
        return



def askUser():
    row = int(input('Enter the row number:'))
    col = int(input('Enter the column number:'))

    if data[row][col] == 9:
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if data[i][j] == 9:
                    prRed('*')
                else:
                    prCyan(play[i][j])
            print()
        return False
    else:
        reveal(row, col)
        display()
        return True




updateMines()
updateNumbers()
display()
actualDisplay()
while askUser():
    pass