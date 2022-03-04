class LanternfishFast:


    def __init__(self,firstGen):
        firstGenList = [0,0,0,0,0,0,0,0,0]
        firstGen = [int(x) for x in firstGen]
        for val in firstGen:
            firstGenList[val] +=1
        self.school = firstGenList
        

    def __str__(self):
        return f"{self.count_fish()}"

    def populate(self):
        '''
        decrements all the fishes intenral timer by one
        this is done by shifting all fish on a specific timer down one slot,
        if the fish is on zero we add new fish both to the 6 and 8 slots.
        '''
        
        fishRefresh = self.school[0]
        del self.school[0]
        self.school.append(fishRefresh)
        self.school[6] +=fishRefresh

   

    def count_fish(self):
        return sum(self.school)