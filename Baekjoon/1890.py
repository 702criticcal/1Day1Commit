def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in [[x + board[x][y], y], [x, y + board[x][y]]]:
            nextX = i[0]
            nextY = i[1]
            if 0 <= nextX < n and 0 <= nextY < n:
                dp[x][y] += dfs(nextX, nextY)
    return dp[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
print(dfs(0, 0))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and board[i][j] != 0:
            if 0 <= i + board[i][j] < n and 0 <= j < n:
                dp[i + board[i][j]][j] += dp[i][j]
            if 0 <= i < n and 0 <= j + board[i][j] < n:
                dp[i][j + board[i][j]] += dp[i][j]
print(dp[-1][-1])
