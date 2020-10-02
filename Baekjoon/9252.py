a = input()
b = input()
a_len = len(a)
b_len = len(b)
dp = [[''] * 1001 for _ in range(1001)]

for i in range(a_len):
    for j in range(b_len):
        # a[i]와 b[j]가 같다면 이전 LCS에서 b[j]를 더해준 것을 dp[i + 1][j + 1]에 저장한다.
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + b[j]
        else:
            # 다르다면 dp[i][j + 1]와 dp[i + 1][j] 중 더 길이가 긴 LCS를 그대로 저장한다.
            if len(dp[i][j + 1]) >= len(dp[i + 1][j]):
                dp[i + 1][j + 1] = dp[i][j + 1]
            else:
                dp[i + 1][j + 1] = dp[i + 1][j]
print(len(dp[a_len][b_len]))
print(dp[a_len][b_len])
