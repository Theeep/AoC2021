from sys import stdin
from Segment import Segment


keys = []
codes =[]
for line in stdin:
    key, code = line.split("|")
    keys.append(key.strip())
    codes.append(code.strip())
print(keys[0])
globalTotal = 0
for key,code in zip(keys,codes):
    new_seg = Segment(key)
    new_seg.assign_trivial()
    new_seg.assign_relational()
    newTotal = int(new_seg.decode(code))
    print(newTotal)
    globalTotal+=newTotal
print(globalTotal)