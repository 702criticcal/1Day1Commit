n = int(input())
num_lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n + 1)]
dp[0] = num_lst[0]

for i in range(n - 1):
    for j in range(len(num_lst[i])):
        dp[i + 1][j] = max(dp[i][j] + num_lst[i + 1][j], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i][j] + num_lst[i + 1][j + 1], dp[i + 1][j + 1])

print(max(dp[-1]))
