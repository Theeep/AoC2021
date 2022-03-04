from Bingo import Bingo
from sys import builtin_module_names, stdin
import re


moves = []
bingoBoards = []
currBoard = []
currBoardCounter = 0
for i,line in enumerate(stdin):
    line = line.strip()
    line = re.sub("\s\s+" , " ", line)
    if i == 0:
        moves = [int(x) for x in line.split(',')]
    elif line!='':
        
        currBoard.append([int(x) for x in line.split(' ')]) 
        currBoardCounter+=1
        if currBoardCounter == 5:
            newBoard = Bingo(currBoard)
            bingoBoards.append(newBoard)
            currBoardCounter = 0
            currBoard = []


for i,move in enumerate(moves):
    for board in bingoBoards:
        board.check_for_number(move)
    if i >=5:
        for board in bingoBoards:
            result = board.check_win()
            if result != False:
                #Part 2 solution
                #If more than one board remain and a board is winning
                #it cannot be the last board to win so we pop it,
                # we do this until there is only one left
                if len(bingoBoards) > 1:
                    bingoBoards.remove(board)
                else:
                    #Normal victory calulation
                    total = board.sum_of_unmarked_squares() * move
                    print(total)
                    exit()
        
