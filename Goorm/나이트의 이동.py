from collections import deque


def bfs(l, chess, start, goal):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    queue = deque()
    queue.append([0, start])

    while queue:
        cnt, current = queue.popleft()

        if current == goal:
            return cnt

        for i in range(8):
            nextX = current[0] + dx[i]
            nextY = current[1] + dy[i]
            if 0 <= nextX < l and 0 <= nextY < l and chess[nextX][nextY] == '0':
                chess[nextX][nextY] = cnt + 1
                queue.append([cnt + 1, [nextX, nextY]])


if __name__ == "__main__":
    l = int(input())
    chess = [['0'] * l for _ in range(l)]
    knight = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    print(bfs(l, chess, knight, goal))