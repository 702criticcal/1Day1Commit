def dfs(x, y, num):
    if len(num) == 6:
        result.add(num)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if 0 <= nextX < 5 and 0 <= nextY < 5:
            dfs(nextX, nextY, num + numLst[nextX][nextY])


if __name__ == "__main__":
    numLst = [list(input().split()) for _ in range(5)]
    result = set()

    for i in range(5):
        for j in range(5):
            dfs(i, j, numLst[i][j])

    print(len(result))
