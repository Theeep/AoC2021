import sys

vert,hori = 0,0
commands = []
for command in sys.stdin:
    commands.append(command.split())

for command in commands:
    if command[0] == "forward":
        vert+=int(command[1])
    elif command[0] == "up":
        hori-=int(command[1])
    elif command[0] == "down":
        hori+=int(command[1])

print(vert*hori)