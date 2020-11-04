def move(board, directions, n):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    s = 1
    board[0][0] = 9
    snake = [[0, 0]]
    startX, startY = 0, 0
    currentDir = 0

    while True:
        nextX = startX + dx[currentDir]
        nextY = startY + dy[currentDir]
        if 0 <= nextX < n and 0 <= nextY < n and board[nextY][nextX] != 9:
            if board[nextY][nextX] != 1:
                endX, endY = snake.pop(0)
                board[endY][endX] = 0
            board[nextY][nextX] = 9
            snake.append([nextX, nextY])

            startX = nextX
            startY = nextY

            if len(directions) > 0 and s == directions[0][0]:
                if directions[0][1] == 'D':
                    currentDir += 1
                    if currentDir == 4:
                        currentDir = 0
                else:
                    currentDir -= 1
                    if currentDir == -1:
                        currentDir = 3

                directions.pop(0)
            s += 1
        else:
            return s


if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        board[x - 1][y - 1] = 1

    l = int(input())
    directions = []
    for _ in range(l):
        sec, dir = input().split()
        directions.append([int(sec), dir])

    print(move(board, directions, n))
