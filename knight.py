import random


def initialize(k):
    population = []
    for i in range(0, k):
        newInd = ''
        for j in range(0, 189):
            newInd += str(random.randrange(0, 2, 1))
        population.append(newInd)

    return population

def fitness(indiv):
    j = 0
    for i in range(0, 63):
        move = ''
        for cont in range(0, 3):
            move += indiv[j]
            j += 1
        print(move)

    return score


pop = initialize(5)

board = []
size = 8
for i in range(0, size):
    row = []
    for j in range(0, size):
        row.append(0)
    board.append(row)


