from sys import stdin
from Dumbo import Dumbo
grid = []
for line in stdin:
    grid.append([int(x) for x in line.strip()])

octo = Dumbo(grid)

print(octo)
total = {}
subTotal = 0
x= 0
while subTotal != 100:
    x+=1
    octo.charge()
    subTotal = octo.flash()
    total[x] = subTotal
print(x)