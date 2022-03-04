from sys import stdin
from Lanternfish import Lanternfish
from LanterfishFast import LanternfishFast

init_state = []
for line in stdin:
    init_state = line.split(',')

fishes = LanternfishFast(init_state)

for i in range(256):
    fishes.populate()
    print(f"{i+1} : {fishes}")

