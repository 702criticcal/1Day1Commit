import sys

sys.setrecursionlimit(100000)


def dfs(hallway, i, j, N, M):
    global trash_cnt
    if i < 0 or i >= N or j < 0 or j >= M or hallway[i][j] != '#':
        return trash_cnt

    hallway[i][j] = '.'
    trash_cnt += 1

    dfs(hallway, i + 1, j, N, M)
    dfs(hallway, i - 1, j, N, M)
    dfs(hallway, i, j + 1, N, M)
    dfs(hallway, i, j - 1, N, M)

    return trash_cnt


N, M, K = map(int, input().split())
hallway = [['.'] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    hallway[a - 1][b - 1] = '#'
answer = 0

for i in range(N):
    for j in range(M):
        if hallway[i][j] == '#':
            trash_cnt = 0
            dfs(hallway, i, j, N, M)
            answer = max(trash_cnt, answer)
print(answer)
