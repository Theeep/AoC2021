class Bingo:
    '''
    Plays bingo, good for a rainy day playing vs a Giant squid
    made for AdventOfCode day4

    Default board size is 5.
    '''


    def __init__(self,board,board_size=5):
        self.boardSize = board_size
        self.__board = board                # Holds both the numberic values of 
                                            #each square and if they've been marked
    
    def __str__(self):
        retStr = '==========\n'
        for line in self.__board:
            retStr+= ','.join(map(str,line)) + "\n"
        retStr+= '==========\n\n'
        return retStr

    def check_win(self):
        '''
        Goes through all the rows and columns calling check_win_line for each.
        '''
        win = False
        for pos in range(self.boardSize):
            if not win:
                win = self.check_win_line(self.__board[pos])
                # if the current row includes a win we return it
                if win:
                    return self.__board[pos] 
            if not win:
                line = self.col_to_line(self.__board,pos)
                win = self.check_win_line(line)
                # same as we did for row but now for columns
                if win:
                    return self.col_to_line(self.__board,pos)
        return False


    def check_win_line(self,line):
        '''
        Returns: True if there is a win in the line otherwise returns False
        '''
        for num in line:
            if num != 'x':
                return False
        return True
    
    def check_for_number(self,move):
        '''
        Initializes x to be "nf" or not found until it has been found then
        Returns a touple of (x,y) coords of a given number if it
        is found within the nrBoard
        '''
        x = "nf"
        for y, line in enumerate(self.__board):
            if x == "nf":
                x = self.check_number_line(line,move)
                if x != "nf":
                    self.mark_square((y,x))
                    return True
        return False

    def check_number_line(self,line,move):
        '''
        Returns: the position of a number if the number is found within the given line
        other wise returns "nf" for not found
        '''
        for i,num in enumerate(line):
            if num == move:
                return i
        return "nf"

    def col_to_line(self,board,pos):
        '''
        Translates column positions to a line so that we can reuse the win check function for row
        '''
        return [board[0][pos],
                board[1][pos],
                board[2][pos],
                board[3][pos],
                board[4][pos]]

    def mark_square(self,pos):
        self.__board[pos[0]][pos[1]] = 'x'

    def sum_of_unmarked_squares(self):
        '''
        Returns: Sum of the value of squares that haven't been marked 
        '''
        sum = 0
        for row in self.__board:
            for val in row:
                if val != 'x':
                    sum+= val
        return sum