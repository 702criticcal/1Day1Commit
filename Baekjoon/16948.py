from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
chess = [[0] * N for _ in range(N)]
chess[r1][c1] = 1
queue = deque([[r1, c1]])

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

while queue:
    x, y = queue.popleft()

    if x == r2 and y == c2:
        print(chess[r2][c2] - 1)
        exit()

    for i in range(6):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N and chess[next_x][next_y] == 0:
            queue.append([next_x, next_y])
            chess[next_x][next_y] = chess[x][y] + 1
print(-1)
