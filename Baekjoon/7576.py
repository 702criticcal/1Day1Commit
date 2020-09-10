from collections import deque


def tomatoes(M, N, box):
    zero_cnt = 0
    for i in box:
        zero_cnt += i.count(0)
    if zero_cnt == 0:
        return 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([])

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append([i, j])

    while queue:
        tomato = queue.popleft()
        x = tomato[0]
        y = tomato[1]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and box[next_x][next_y] == 0:
                queue.append([next_x, next_y])
                box[next_x][next_y] = box[x][y] + 1

    day = 0
    for i in box:
        if 0 in i:
            return -1
        else:
            if day < max(i):
                day = max(i)
    return day - 1


M, N = map(int, input().split())
box = [list(map(int, input().split(' '))) for _ in range(N)]
print(tomatoes(M, N, box))
