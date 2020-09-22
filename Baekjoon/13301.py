N = int(input())
fibonacci = [1] * (N + 1)
dp = [0] * (N + 1)
dp[1] = 4

for i in range(3, N + 1):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + fibonacci[i] * 2

print(dp[N])
