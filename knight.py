import random


def initialize(k, size):
    population = []
    for i in range(0, k):
        newInd = ''
        for j in range(0, (size * size * 3) - 3):
            newInd += str(random.randrange(0, 2, 1))
        population.append([newInd, 0])

    return population


def walk(move, board, pos):
    out = False

    if move == '000':
        pos[0] += 2
        pos[1] += 1
    elif move == '001':
        pos[0] += 1
        pos[1] += 2
    elif move == '010':
        pos[0] -= 1
        pos[1] += 2
    elif move == '011':
        pos[0] -= 2
        pos[1] += 1
    elif move == '100':
        pos[0] -= 2
        pos[1] -= 1
    elif move == '101':
        pos[0] -= 1
        pos[1] -= 2
    elif move == '110':
        pos[0] += 1
        pos[1] -= 2
    else:
        pos[0] += 2
        pos[1] -= 1

    try:
        if pos[0] < 0 or pos[1] < 0:
            out = True
        else:
            board[pos[0]][pos[1]] += 1
    except IndexError:
        out = True

    return [board, pos, out]


def fitness(indiv, size):
    board = []

    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(0)
        board.append(row)

    pos = [0, 0]
    board[pos[0]][pos[1]] += 1

    score = 0

    j = 0
    for i in range(0, (size * size) - 1):
        move = ''
        for cont in range(0, 3):
            move += indiv[j]
            j += 1
        board, pos, out = walk(move, board, pos)
        if out:
            score -= 10

    for row in board:
        for elem in row:
            if elem == 1:
                score += 5
            elif elem == 0:
                pass
            else:
                score -= elem

    return [score, board]


def selection(population):
    population.sort(key=lambda x: x[1])
    n = len(population)
    pool = []

    for i in range(0, 2 * n):
        while True:
            ind = random.choice(range(0, n))
            coef = random.choice(range(population[0][1] - 1, population[n-1][1]))

            if coef < population[ind][1]:
                break

        pool.append(population[ind][0])

    return pool

def crossover(pool):
    n = len(pool)
    newPop = []
    for i in range(0,n,2):
        indiv1 = pool[i]
        indiv2 = pool[i+1]

        tamcadeia = len(indiv1)
        splitPoint = random.choice(range(0,tamcadeia))

        # Gerando dois indivíduos MUDAR SE FICAR BOSTA QUE NEM O ALVARO LIXO
        novoIndiv1 = indiv1[:splitPoint] + indiv2[splitPoint:]

        #FAZENDO A MUTAÇÃO
        if(100 * random.random() < mutationRate):
            numMutations = random.choice(range(1,size))
            for j in range(0,numMutations):
                x = random.choice(range(0,len(indiv1)))
                if novoIndiv1[x] == '0':
                    novoIndiv1 = novoIndiv1[:x] + '1' + novoIndiv1[x+1:]
                else:
                    novoIndiv1 = novoIndiv1[:x] + '0' + novoIndiv1[x+1:]

        newPop.append([novoIndiv1, 0])
        #newPop.append([novoIndiv2, 0])

    return newPop

mutationRate = 30
size = 6
k = 1000
numIt = 1000
population = initialize(k, size)


for it in range(0, numIt):
    print("GENERATION " + str(it))

    for x in range(0, k):
        population[x][1], board = fitness(population[x][0], size)

    matingPool = selection(population)

    population.sort(key=lambda x: x[1], reverse=True)
    print('BEST GUY: ' + str(population[0][1]))
    _, board = fitness(population[0][0], size)
    for row in board:
        print(row)

    population = crossover(matingPool)
