
class Basin:

    def __init__(self,readings) -> None:
        self.readings = readings
        self.marked = set()
        self.highY = len(readings)-1
        self.highX = len(readings[0])-1

    def __str__(self):
        retStr = ''
        for i,row in enumerate(self.marked):
            retStr+= f"{i+1} -> {''.join(row)}\n"
        return retStr
   
    def reset_marked(self):
        self.marked = set()

    def mark_square(self,Y,X):
        self.marked.add((Y,X))

    def boundry_check(self,curr,nxt,comp,high=0):
        '''
        Boundry checking moved away from other functions
        and made slightly more general so it can be used in both in 
        the low_point and basin functions
        '''
        if high == 0:
            if comp != 0:
                if self.readings[curr[0]][curr[1]] < self.readings[nxt[0]][nxt[1]]:
                    return True
        elif high != 0:
            if comp <=high:
                if self.readings[curr[0]][curr[1]] < self.readings[nxt[0]][nxt[1]]:
                    return True
        return False

   
    def low_point(self,Y,X):
        '''
        Simple boundry checker, to that makes sure we arent checking outside the list
        '''
        lowCounter = 0
        #check North
        if self.boundry_check((Y,X),(Y-1,X),Y):
            lowCounter+=1
        #check South
        if self.boundry_check((Y,X),(Y+1,X),Y+1,self.highY):
            lowCounter+=1
        #check West
        if self.boundry_check((Y,X),(Y,X-1),X):
            lowCounter+=1
        #check East
        if self.boundry_check((Y,X),(Y,X+1),X+1,self.highX):
            lowCounter+=1
        #Accounting for edges
        if X == 0 or X == self.highX:
            lowCounter+=1
        if Y == 0 or Y == self.highY:
            lowCounter+=1
        if lowCounter==4:
            return True
        else:
            return False
    
    def find_basin(self,Y,X):

        #langar að færa þetta hingað
        #þarf að passa að marka ekki níur, en ég ætti aldrei að skoða níur
        #Þetta var vandamálið
        #þetta var það :C
        #FML
        self.mark_square(Y,X)
        #check North
        if self.boundry_check((Y,X),(Y-1,X),Y):
            if (Y-1,X) not in self.marked and self.readings[Y-1][X]!=9:
                self.find_basin(Y-1,X)
        #check South
        if self.boundry_check((Y,X),(Y+1,X),Y+1,self.highY):
            if (Y+1,X) not in self.marked and self.readings[Y+1][X]!=9:
                self.find_basin(Y+1,X)
        #check West
        if self.boundry_check((Y,X),(Y,X-1),X):
            if (Y,X-1) not in self.marked and self.readings[Y][X-1]!=9:
                self.find_basin(Y,X-1)
        #check East
        if self.boundry_check((Y,X),(Y,X+1),X+1,self.highX):
            if (Y,X+1) not in self.marked and self.readings[Y][X+1]!=9:
                self.find_basin(Y,X+1)

    def size_of_basin(self):
        return len(self.marked)


    def find_low_points(self):
        '''
        Finds all low points in self.readings, 
        then if a low point is found it searches for a basin out 
        from that lowpoint
        '''
        #A list of all low points
        basins = []
        for y,row in enumerate(self.readings):
            for x,value in enumerate(row):
                
                if self.low_point(y,x):
                    #check for basin
                    self.find_basin(y,x)
                    
                    basins.append(self.size_of_basin())
                    self.reset_marked()
        return basins