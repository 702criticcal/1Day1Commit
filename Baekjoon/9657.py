n = int(input())
dp = [0, 1, 0, 1, 1]  # 1:상근, 0:창영.

for i in range(5, n + 1):
    if dp[i - 4] + dp[i - 3] + dp[i - 1] < 3:
        dp.append(1)
    else:
        dp.append(0)

print("SK" if dp[n] == 1 else "CY")
