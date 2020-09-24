def solution(m, n, puddles):
    # 경로의 수 계산할 dp 리스트.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            # 물에 잠긴 지역이라면 0으로 값 고정.
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                # 갈 수 있는 지역이면 오른쪽과 아래쪽으로만 움직일 수 있으므로 왼쪽과 위의 경우의수를 더해줌.
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
