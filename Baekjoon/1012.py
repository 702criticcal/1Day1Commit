import sys

sys.setrecursionlimit(100000)


def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return

    grid[i][j] = 0

    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    Farm = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        Farm[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if Farm[i][j] == 1:
                dfs(Farm, i, j)
                cnt += 1
    print(cnt)
