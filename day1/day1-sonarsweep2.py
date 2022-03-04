import sys

numList = []
for num in sys.stdin:
    numList.append(int(num))

a,b,c,prev,inc= 0,0,0,0,0

for i in range(len(numList)-2):
    a = numList[i]
    b = numList[i+1]
    c = numList[i+2]
    window = a+b+c
    if window>prev:
        inc+=1
    prev = window
print(inc)

