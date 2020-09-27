n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
dp = [0, wines[1]]
if n >= 2:
    dp.append(wines[1] + wines[2])
for i in range(3, n + 1):
    # i번째 포도주를 먹지 않거나, i-2번째 포도주를 먹지 않거나, i-1번째 포도주를 먹지 않은 것 중에 최댓값 append.
    dp.append(max(dp[i - 1], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i]))
print(dp[n])
