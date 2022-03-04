import sys

aim,vert,depth = 0,0,0
commands = []
for command in sys.stdin:
    commands.append(command.split())

for command in commands:
    if command[0] == "forward":
        vert+=int(command[1])
        depth+=int(command[1])*aim

    elif command[0] == "up":
        aim-=int(command[1])
    elif command[0] == "down":
        aim+=int(command[1])

print(depth*vert)