from Vents import Vents
from sys import stdin

vent_before = []
vent_after  = []

for line in stdin:
    a,b = line.strip().split(' -> ')
    vent_before.append(tuple(map(int,a.split(','))))
    vent_after.append(tuple(map(int,b.split(','))))

# find the maximum tuple then the maximal value in that tuple might not work if the second value is the largest
max_before = max(max(vent_before)) + 1
max_after =  max(max(vent_after))  + 1

if(max_before>max_after):
    hydrovents = Vents(max_before,max_before)
else:
    hydrovents = Vents(max_after,max_after)

for vb,va in zip(vent_before,vent_after):
    cvb,cva = hydrovents.greater_pos(vb,va)
    hydrovents.generate_line(cvb,cva)

print(hydrovents.count_over_two())


