for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    dp[0][1], dp[1][1] = sticker[1][0] + sticker[0][1], sticker[0][0] + sticker[1][1]

    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[0][j - 2], dp[1][j - 2], dp[1][j - 1]) + sticker[i][j]
            else:
                dp[i][j] = max(dp[0][j - 2], dp[1][j - 2], dp[0][j - 1]) + sticker[i][j]

    print(max(dp[0][-1], dp[1][-1]))
