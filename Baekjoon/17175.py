dp = [1, 1]
for i in range(2, int(input()) + 1):
    dp.append(dp[i - 1] + dp[i - 2] + 1)
print(dp[-1] % 1000000007)
