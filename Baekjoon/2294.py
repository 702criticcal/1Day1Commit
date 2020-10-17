import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
coins = []

for _ in range(n):
    coins.append(int(input()))

for i in range(1, k + 1):
    temp = []

    for j in coins:
        if j <= i and dp[i - j] != -1:
            temp.append(dp[i - j] + 1)

    if not temp:
        dp[i] = -1
    else:
        dp[i] = min(temp)

print(dp[k])
