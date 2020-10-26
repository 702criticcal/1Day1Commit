from collections import deque


def bfs():
    while waterQueue or hedgehogQueue:
        hedgehogTemp = []
        waterTemp = []

        while hedgehogQueue:
            x, y = hedgehogQueue.popleft()
            if map[x][y] != '*':
                for i in range(4):
                    nextX = x + dx[i]
                    nextY = y + dy[i]
                    if 0 <= nextX < R and 0 <= nextY < C and map[nextX][nextY] != 'X' and map[nextX][nextY] != '*' and \
                            visited[nextX][nextY] == 0:
                        map[nextX][nextY] = map[x][y] + 1
                        visited[nextX][nextY] = 1
                        hedgehogTemp.append([nextX, nextY])

        while waterQueue:
            x, y = waterQueue.popleft()
            for i in range(4):
                nextX = x + dx[i]
                nextY = y + dy[i]
                if nextX == dX and nextY == dY:
                    continue
                if 0 <= nextX < R and 0 <= nextY < C and map[nextX][nextY] != 'X' and map[nextX][nextY] != '*':
                    map[nextX][nextY] = '*'
                    waterTemp.append([nextX, nextY])

        for i in hedgehogTemp:
            hedgehogQueue.append(i)
        for i in waterTemp:
            waterQueue.append(i)


if __name__ == "__main__":
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    waterQueue = deque([])
    hedgehogQueue = deque([])

    R, C = map(int, input().split())
    map = []
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        map.append(list(input()))
        for j in range(C):
            if map[i][j] == 'D':
                dX, dY = i, j
            elif map[i][j] == 'S':
                s = [i, j]
                hedgehogQueue.append([i, j])
                visited[i][j] = 1
                map[i][j] = 0
            elif map[i][j] == '*':
                waterQueue.append([i, j])

    bfs()

    print(map[dX][dY] if map[dX][dY] != 'D' else "KAKTUS")
