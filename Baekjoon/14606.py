N = int(input())
dp = [0] * 11
dp[1], dp[2] = 0, 1

for i in range(3, N + 1):
    if i % 2 == 1:
        dp[i] = (i // 2) * (i // 2 + 1) + dp[i // 2] + dp[i // 2 + 1]
    else:
        dp[i] = (i // 2) * (i // 2) + dp[i // 2] + dp[i // 2]

print(dp[N])
