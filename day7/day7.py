from sys import stdin



def avg(l):
    return round(sum(l)/len(l))

def calc_fuel(list,pos):
    totalCost = 0
    for crab in list:
        n = abs((crab-pos))
        addition = (n*(n+1)/2)
        totalCost+= addition
    return totalCost

def crab_check(crabs):
    crabAvg = avg(crabs)
    maxCrab = max(crabs)
    minCrab = min(crabs)

    delta = maxCrab-minCrab
    rngeLow = round(delta//2 -crabAvg) 
    rngeLow = minCrab if rngeLow < minCrab else rngeLow
    rngeHigh = round(delta//2 + crabAvg)
    rngeHigh = maxCrab if rngeHigh > maxCrab else rngeHigh
    fuelCosts = []

    for i in range(rngeLow,rngeHigh):
        fuelCosts.append(calc_fuel(crabs,i))

    return fuelCosts
crabs = []
for line in stdin:
    crabs = [int(x) for x in line.split(',')] 

print(min(crab_check(crabs)))






