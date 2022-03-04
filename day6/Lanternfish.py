class Lanternfish:
    #misunderstood the prompt
    #INTERNAL_TIMER = 6
    def __init__(self,first_gen):
        self.school = {0:[int(x) for x in first_gen]}
        

    def __str__(self):
        return f"{self.count_fish()}"

    def populate(self):
        '''
        decrements all the fishes intenral timer by one
        '''
        #If we need a new generation we add those fish to this dict, then patch it to the main on after the loop
        maxKey = max(self.school.keys())
        newSchool = {(maxKey+1):[]}
        #Go through all generations starting with the highest
        for gen,school in reversed(self.school.items()):
            #for each fish in that current generation decrement its IT by one 
            for i,fish in enumerate(school):
                if school[i] == 0:
                    #if it is at zero we reset it to max
                    school[i] = 6
                    # and add another fish to the next generation
                    if (gen+1) in self.school:
                        #if the next generation exists we retrieve that list and append to it
                        #a new fish with the corresponding interal timer
                        self.school[gen+1].append(8)
                    else:
                        newSchool[gen+1].append(8)
                else:
                    #otherwise we just remove one from the internal timer then move on
                    school[i] -= 1
        if(newSchool[maxKey+1]!= []):
            self.school.update(newSchool)
    #misunderstood the prompt, might be useful in part 2
    #thought each generation was supposed to have its own independant Internal Timer
    #def __get_timer(self,gen):
    #    return 2*gen + self.INTERNAL_TIMER


    def count_fish(self):
        total = 0
        for k,v in self.school.items():
            total+= len(v)
        return total