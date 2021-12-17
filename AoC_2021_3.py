import numpy as np

matrix = np.genfromtxt('AoC_Input_2021_3.txt', delimiter=1, dtype=int)
meanColls = np.round(matrix.mean(axis=0))

potens = len(meanColls)

gamma = 0
epsilon = 0
for i in meanColls:
    potens = potens-1
    gamma = gamma + i*2**potens
    epsilon = epsilon + abs(i-1)*2**potens

print(gamma*epsilon)

oxigenMatrix = matrix
for idx in range(len(matrix[0])):
    mostCommon = np.round(oxigenMatrix.mean(axis=0)+0.00000000001)
    oxigenMatrix = oxigenMatrix[oxigenMatrix[:, idx] == mostCommon[idx]]
    print(oxigenMatrix)

print('Oxegen Matrix')
print(oxigenMatrix)

coTwoMatrix = matrix
for idx in range(len(matrix[0])):
    mostCommon = np.round(coTwoMatrix.mean(axis=0)+0.00000000001)
    coTwoMatrix = coTwoMatrix[coTwoMatrix[:, idx] != mostCommon[idx]]
    if(len(coTwoMatrix) == 1):
        print('breaking')
        break

print('CO2Matrix')
print(len(coTwoMatrix))

potens = len(meanColls)
oxygenGeneratorRating = 0
coTwoGeneratorRating = 0
for (i, j) in zip(oxigenMatrix[0], coTwoMatrix[0]):
    potens = potens-1
    oxygenGeneratorRating = oxygenGeneratorRating + i*2**potens
    coTwoGeneratorRating = coTwoGeneratorRating + j*2**potens

print(oxygenGeneratorRating*coTwoGeneratorRating)
