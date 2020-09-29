import sys

sys.setrecursionlimit(100000)


def dfs(grid, i, j, N, area):
    if i < 0 or i >= N or j < 0 or j >= N or grid[i][j] != area:
        return

    grid[i][j] = 0

    dfs(grid, i + 1, j, N, area)
    dfs(grid, i - 1, j, N, area)
    dfs(grid, i, j + 1, N, area)
    dfs(grid, i, j - 1, N, area)


N = int(input())
grid = [input() for _ in range(N)]
normal_grid = [list(i) for i in grid]
color_blindness_grid = [list(i.replace('R', 'G')) for i in grid]
answer = [0, 0]

for i in range(N):
    for j in range(N):
        if normal_grid[i][j] in ['R', 'G', 'B']:
            dfs(normal_grid, i, j, N, normal_grid[i][j])
            answer[0] += 1

for i in range(N):
    for j in range(N):
        if color_blindness_grid[i][j] in ['G', 'B']:
            dfs(color_blindness_grid, i, j, N, color_blindness_grid[i][j])
            answer[1] += 1

print(answer[0], answer[1])
