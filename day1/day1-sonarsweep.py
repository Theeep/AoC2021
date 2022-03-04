import sys

inc = 0 
prev = '-1'
for sweep in sys.stdin:
    if sweep>prev: inc+=1
    prev = sweep

print(inc)
