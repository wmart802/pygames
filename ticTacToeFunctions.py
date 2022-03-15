# Functions for Tic Tac Toe Game

def checkwinner(boardspots):
    winner = False
    # Check three across
    if boardspots[0] == boardspots[1] == boardspots[2]:
        winner = boardspots[0]
    elif boardspots[3] == boardspots[4] == boardspots[5]:
        winner = boardspots[3]
    elif boardspots[6] == boardspots[7] == boardspots[8]:
        winner = boardspots[6]
    # Check three vertically
    elif boardspots[0] == boardspots[3] == boardspots[6]:
        winner = boardspots[0]
    elif boardspots[1] == boardspots[4] == boardspots[7]:
        winner = boardspots[1]
    elif boardspots[2] == boardspots[5] == boardspots[8]:
        winner = boardspots[2]
    # Check diagonals
    elif boardspots[0] == boardspots[4] == boardspots[8]:
        winner = boardspots[0]
    elif boardspots[2] == boardspots[4] == boardspots[6]:
        winner = boardspots[2]

    return winner