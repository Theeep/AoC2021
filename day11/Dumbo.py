class Dumbo:

    def __init__(self,grid):
        self.grid = grid
        self.gridSize = len(grid)-1
        self.alreadyFlashed = set()


    def __str__(self):
        retStr = ""
        for row in self.grid:
            retStr += f"{row} \n"
        return retStr

    def reset_flashed(self):
        for (y,x) in self.alreadyFlashed:
            self.grid[y][x] = 0
        self.alreadyFlashed = set()

    def flash(self):
        for y in range(self.gridSize+1):
            for x in range(self.gridSize+1):
                self.flash_single(y,x)

        totalFlashed = len(self.alreadyFlashed)
        self.reset_flashed()
        return totalFlashed

    def flash_single(self,y,x):
        if self.grid[y][x] > 9 and (y,x) not in self.alreadyFlashed:
            self.alreadyFlashed.add((y,x))
            self.directional_checks(y,x)

    def charge(self):
        for y in range(self.gridSize+1):
            self.grid[y] = [x+1 for x in self.grid[y]]
            

    def directional_checks(self,y,x):
        directions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

        for dir in directions:
            currY = dir[1]+y
            currX = dir[0]+x
            if 0 <= currY <= self.gridSize and 0 <= currX <= self.gridSize:
                self.grid[currY][currX] +=1
                self.flash_single(currY,currX)
                #do something