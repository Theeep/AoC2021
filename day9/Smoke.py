from sys import stdin
from math import prod
from Basin import Basin

readings = []

for line in stdin:
    readings.append([int(x) for x in line.strip()])


#The prompt askes us to return the sum of all low points + the amount of low points
#print(lowPoints)

basin = Basin(readings)
#Find low points loops through all readings to find a low point
#then if a low point is found it finds a basin then returns the size of that basin
basins = basin.find_low_points()

basins.sort(reverse=True)
print(prod(basins[:3]))