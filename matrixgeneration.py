from random import *

def bombgeneration(n, m, bombnumber):
    bombmap = [[0]*m for x in range(n)]
    for i in range(bombnumber):
        x = randint(0, n-1)
        y = randint(0, m-1)
        # print(f"{x} and {y}")
        while bombmap[x][y] == 1:
            x = randint(0, n-1)
            y = randint(0, m-1)
            # print(f"{x} and {y}")
        bombmap[x][y] = 1
        # print(bombmap[x][y])
    return bombmap


def squaresearch(matrix, n, m, i, j):
    df = [1, 0, -1, 0, 1, 1, -1, -1]
    ds = [0, 1, 0, -1, 1, -1, -1, 1]
    count = 0
    for x in range(8):
        copyi = i + df[x]
        copyj = j + ds[x]
        if 0 <= copyi < n and 0 <= copyj < m:
            if matrix[copyi][copyj] == 1:
                count += 1
    return count


def bombsneighbourhood(bombmap, n, m):
    neighbours = [[0]*m for x in range(n)]
    for i in range(n):
        for j in range(m):
            if bombmap[i][j] == 0:
                neighbours[i][j] = squaresearch(bombmap, n, m, i, j)
            else:
                neighbours[i][j] = 9
    return neighbours
