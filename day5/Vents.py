class Vents:

    def __init__(self,x,y):
        self.__grid = [['.']*x for i in range(y)]

    def __str__(self):
        retStr = '------------------\n'
        for line in self.__grid:
            retStr += ''.join(map(str,line)) + '\n'
        retStr+= '------------------\n'
        return retStr

    def generate_line(self,pos1,pos2):
        '''
        Calls either generate_straight_line or generate_diagonal_line
        depending on which type of line it is, this is determined by
        the straight_or_dia function.
        '''
        if self.straight_or_dia(pos1,pos2):
            self.generate_diagonal_line(pos1,pos2)
        else:
            self.genereate_straight_line(pos1,pos2)


    def generate_diagonal_line(self,pos1,pos2):
        '''
        Finds which way the line should be generated from pos1 to pos2
        via checking which endpoints are higher/lower
        then calls mark_line for the entire line
        '''
        line = [pos1]
        xHighLow = -1 if pos1[0] > pos2[0] else 1
        yHighLow = -1 if pos1[1] > pos2[1] else 1
        delta = abs(pos1[0] - pos2[0])
        for val in range(delta):
            newX = line[-1][0] + xHighLow
            newY = line[-1][1] + yHighLow
            line.append((newX,newY))
        self.mark_line(line)

    def straight_or_dia(self,pos1,pos2):
        '''
        If the points form a diagonal line then the delta of both coordinates will be the same.
        '''
        a = abs((pos1[0] - pos2[0]))
        b = abs((pos1[1] - pos2[1]))
        if a == b:
            return True
        return False

    def genereate_straight_line(self,pos1, pos2):
        '''
        This function generates a line between two positions,
        it assumes that pos1 < pos2 always
        '''
        line = []
        if pos1[0] == pos2[0]:
                line = [(pos1[0],i) for i in range(pos1[1],pos2[1]+1)]
        elif pos1[1] == pos2[1]:
                line = [(i,pos1[1]) for i in range(pos1[0],pos2[0]+1)]

        #after generating a line, we mark all positions in that line
        if line != []:
            self.mark_line(line)

    
    def greater_pos(self,pos1,pos2):
        '''
        Takes in two positions pos1 and pos2 and returns them in ascending order
        '''
        if(pos1[0]<pos2[0]):
            return pos1,pos2
        elif(pos1[0]> pos2[0]):
            return pos2,pos1
        elif(pos1[1]<pos2[1]):
            return pos1,pos2
        else:
            return pos2,pos1
        

    def mark_line(self, line):
        '''
        Line should be a sequence of x,y positions from any pos1 to any pos2
        Increments the grid value by one where the line intesects
        '''

        for pos in line:
            x,y = pos
            if self.__grid[y][x] == '.':
                self.__grid[y][x] = 1
            else:
                val = self.__grid[y][x]
                self.__grid[y][x] = val + 1

    def count_over_two(self):
        '''
        To satisfy the AdventOfCode problem we must be able to calculate
        the total number of squares where two or more lines intersect.
        this function does that C:
        '''
        total = 0
        for line in self.__grid:
            for item in line:
                if isinstance(item,int) and item >= 2:
                    total +=1
        return total