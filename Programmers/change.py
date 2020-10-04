# 1차 코드. 2차원 배열 dp 사용.
def solution(n, money):
    dp = [[0 for _ in range(n + 1)] for _ in range(len(money))]
    dp[0][0] = 1
    for i in range(money[0], n + 1, money[0]):
        dp[0][i] = 1
    for y in range(1, len(money)):
        for x in range(n + 1):
            if x >= money[y]:
                dp[y][x] = (dp[y - 1][x] + dp[y][x - money[y]]) % 1000000007
            else:
                dp[y][x] = dp[y - 1][x]

    return dp[-1][-1]


# 2차 코드. 1차원 배열 dp 사용.
def solution(n, money):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in money:
        for j in range(1, n + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    return dp[n]