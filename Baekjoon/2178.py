from collections import deque

# 이 방법을 통한 4방향 탐색을 처음 시도해봤는데, 재귀를 이용하지 않은 반복문을 통한 탐색 구현하는 것에 힘들어하고 있었는데,
# 앞으로 반복문을 통한 큐나 스택으로 구현하는 코드에는 이 방법을 이용하면 좋겠다.
# (+) bfs는 재귀 구현이 안되니 이 방법을 더욱 연습해야 겠다. bfs, dfs 둘 다 쓰일 수 있으니.
# 각각 인덱스마다 상, 하, 좌, 우를 뜻함.
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
queue = deque([[0, 0]])
maze[0][0] = 1

while queue:
    point = queue.popleft()
    x = point[0]
    y = point[1]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and maze[next_x][next_y] == '1':
            queue.append([next_x, next_y])
            maze[next_x][next_y] = maze[x][y] + 1
print(maze[N - 1][M - 1])
