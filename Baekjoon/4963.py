# 1차 시도. 런타임 에러 실패.
import sys

def dfs(grid, i, j):
    # i나 j가 각각 h와 w를 벗어나거나 육지가 아닌 경우 종료
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return
    # 다시 탐색하지 않기 위해 값을 '0'으로 변경
    grid[i][j] = '0'
    # 동서남북, 대각선 탐색
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i - 1, j - 1)
    dfs(grid, i - 1, j + 1)
    dfs(grid, i + 1, j - 1)
    dfs(grid, i + 1, j + 1)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    count = 0
    grid = [list(sys.stdin.readline().split()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    print(count)

# 2차 시도. 성공.
# 도저히 모르겠어서 구글링을 했는데 일단 파이썬으로 재귀로 풀이한 풀이가 거의 없어서 찾기 힘들었는데,
# 파이썬의 기본 재귀 깊이 제한이 약 1000 정도 인것을 이 문제를 통해 알게 되었다.
# sys.setrecursionlimit(100000)을 통해 재귀 깊이 제한을 늘려서 해결했다.
import sys
sys.setrecursionlimit(100000)

def dfs(grid, i, j):
    # i나 j가 각각 h와 w를 벗어나거나 육지가 아닌 경우 종료
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return
    # 다시 탐색하지 않기 위해 값을 '0'으로 변경
    grid[i][j] = '0'
    # 동서남북, 대각선 탐색
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i - 1, j - 1)
    dfs(grid, i - 1, j + 1)
    dfs(grid, i + 1, j - 1)
    dfs(grid, i + 1, j + 1)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    count = 0
    grid = [list(sys.stdin.readline().split()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    print(count)
