file = open('AoC_Input_2021_2.txt')

forwardSteps = 0
depth = 0
aim = 0
for acction in file.read().splitlines():
    act, scale = acction.split(' ')
    scale = int(scale)
    if(act == 'forward'):
        forwardSteps = forwardSteps + scale
        depth = depth + aim*scale
    elif(act == 'up'):
        #height = height - scale
        aim = aim - scale
    elif(act == 'down'):
        #height = height + scale
        aim = aim + scale

print(forwardSteps*depth)
