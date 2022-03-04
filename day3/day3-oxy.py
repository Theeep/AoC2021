import sys

bitstrings = []
out = []
for bitstr in sys.stdin:
    bitstrings.append(bitstr.strip())


def most_common(bitlist,pos):
    avg = sum([int(x[pos]) for x in bitlist])/len(bitlist)
    return round(avg)

for pos in range(len(bitstrings[0])):
    most = most_common(bitstrings,pos)
    out.append(most)

print(out)

