file = open('AoC_Input_2021_1.txt')

depthMeasurement = map(int, file.read().splitlines())

numDecreased = 0
for i in range(len(depthMeasurement)-1):
    if(depthMeasurement[i] > depthMeasurement[i+1]):
        numDecreased = numDecreased + 1

print('NumDecreased: ' + str(numDecreased))

numDecreased = 0
for i in range(len(depthMeasurement)-3):
    if(depthMeasurement[i] < depthMeasurement[i+3]):
        numDecreased = numDecreased + 1

print('sum3:' + str(numDecreased))
