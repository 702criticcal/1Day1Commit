import sys
sys.setrecursionlimit(100000)


def dfs(grid, i, j):
    global areaCnt
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return areaCnt

    grid[i][j] = 0
    areaCnt += 1

    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)

    return areaCnt


M, N, K = map(int, sys.stdin.readline().split())
paper = [[1] * N for _ in range(M)]
count = 0
area = []

for _ in range(K):
    leftX, rowY, rightX, highY = map(int, sys.stdin.readline().split())
    for i in range(rowY, highY):
        for j in range(leftX, rightX):
            if paper[i][j] == 1:
                paper[i][j] = 0

for i in range(M):
    for j in range(N):
        if paper[i][j] == 1:
            areaCnt = 0
            dfs(paper, i, j)
            area.append(areaCnt)
            count += 1
print(count)
print(' '.join(list(map(str, sorted(area)))))
