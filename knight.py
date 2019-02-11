import random


def initialize(k):
    population = []
    for i in range(0, k):
        newInd = ''
        for j in range(0, 189):
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


def fitness(indiv, board, pos):
    score = 0

    j = 0
    for i in range(0, 63):
        move = ''
        for cont in range(0, 3):
            move += indiv[j]
            j += 1
        board, pos, out = walk(move, board, pos)
        if out:
            score -= 5

    for row in board:
        for elem in row:
            if elem == 1:
                score += 1
            elif elem == 0:
                pass
            else:
                score -= 1 - elem

    return [score, board, pos]


def selection(population):
    population.sort(key=lambda x: x[1])
    n = len(population)
    pool = []

    for i in range(0, n):
        while True:
            ind = random.choice(range(0, n))
            coef = random.choice(range(population[0][1], population[n-1][1]))

            if coef < population[ind][1]:
                break

        pool.append(population[ind][0])
        print(ind)

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
        novoIndiv2 = indiv2[:splitPoint] + indiv1[splitPoint:]

        newPop.append(novoIndiv1)
        newPop.append(novoIndiv2)
    
    return newPop


size = 8
k = 10
population = initialize(k)
random.seed(10)

scores = []
for x in range(0, k):
    board = []

    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(0)
        board.append(row)

    pos = [3, 4]
    board[pos[0]][pos[1]] += 1

    population[x][1], board, pos = fitness(population[x][0], board, pos)

matingPool = selection(population)
population = crossover(matingPool)
