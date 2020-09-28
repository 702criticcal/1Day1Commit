from collections import deque

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for _ in range(int(input())):
    I = int(input())
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    chess = [[0] * I for _ in range(I)]
    queue = deque([[start_x, start_y]])
    chess[start_x][start_y] = 1

    while queue:
        point = queue.popleft()
        x = point[0]; y = point[1]
        if [x, y] == [goal_x, goal_y]:
            break
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < I and 0 <= next_y < I and chess[next_x][next_y] == 0:
                queue.append([next_x, next_y])
                chess[next_x][next_y] = chess[x][y] + 1
    print(chess[goal_x][goal_y] - 1)
