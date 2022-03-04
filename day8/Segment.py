class Segment:



    def __init__(self,symbols):
        self.symbols = [''.join(sorted(x)) for x in symbols.split(" ")]
        #these should realistically just be in a list or dictionary, 
        #but I found it easier to think about the union/intersects this way
        self.keys = {}

    def __str__(self):
        retStr = ''
        for k,v in self.keys.items():
            retStr+= f"{k}-> {v} \n"
        return retStr

    def assign_trivial(self):
        '''
        These are the symbols we can easily assign due to them having a 
        unique amount of "lines" in them
        '''
        for symbol in self.symbols:
            if len(symbol) == 2:
                self.keys[1] = symbol 
            if len(symbol) == 3:
                self.keys[7] = symbol
            if len(symbol) == 4:
                self.keys[4] = symbol
            if len(symbol) == 7:
                self.keys[8] = symbol

    def assign_relational(self):
        '''
        Here we assign the rest of the symbols,
        there are three of length 5 and three of length 6
        len 5 rules: 
            - 4 intersect 1 will give us a line combination only found in the number 5
            - 2 does not include both symbols of one
            - and 3 is the only remaining after these operations

        len 6 rules:
        These are easier than len 5 because we already have most our symbols
            -6 is the union of 2 and 4
            -9 is the union of 4 and 3
            -and 0 is the only one of len 6 left
        '''

        fives, sixes = set(),set()
        for symbol in self.symbols:
            if len(symbol) == 5:
                fives.add(symbol)
            if len(symbol) == 6:
                sixes.add(symbol)
        ## Fives
        self.set_fives(fives)
        ## Sixes
        self.set_sixes(sixes)
        
    def set_fives(self,fives):
        fourExceptOne = self.diff(self.keys[4],self.keys[1])
        for five in fives:
            if len(self.union(fourExceptOne,five)) == 5:
                self.keys[5] = five
        #removing the five we have found now we have two elements in our set
        fives.remove(self.keys[5])
        fiveOne = fives.pop()
        fiveTwo = fives.pop()
        if len(self.union(self.keys[1],fiveOne)) == len(fiveOne):
            self.keys[3] = fiveOne
            self.keys[2] = fiveTwo
        else:
            self.keys[2] = fiveOne
            self.keys[3] = fiveTwo

    def set_sixes(self,sixes):
        self.keys[9] = self.union(self.keys[4],self.keys[3])
        sixes.remove(self.keys[9])
        sixOne = sixes.pop()
        sixTwo = sixes.pop()
        diffFive = self.diff(sixOne,self.keys[5])
        if len(diffFive) == 1:
            self.keys[6] = sixOne
            self.keys[0] = sixTwo
        else:
            self.keys[6] = sixTwo
            self.keys[0] = sixOne

        

    def decode(self,code):
        total = ''
        code = [''.join(sorted(x)) for x in code.split(" ")]

        for item in code:
            for k,v in self.keys.items():
                if item == v:
                    total+=str(k)
        return total

    def union(self,a,b):
        uni = set(a) | set(b)
        return ''.join(sorted(''.join(uni)))

    def diff(self,a,b):
        inter = set(a) - set(b)
        return ''.join(sorted(''.join(inter)))
