n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [stairs[0]]

for i in range(1, n):
    if i == 1:
        dp.append(max(dp[i - 1] + stairs[i], stairs[i]))
    elif i == 2:
        dp.append(max(dp[i - 2] + stairs[i], stairs[i - 1] + stairs[i]))
    else:
        dp.append(max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2]))
print(dp[-1])
