# 오늘 푼 백준 1932 정수 삼각형과 동일한 문제.
def solution(triangle):
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0] = triangle[0]

    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i][j] + triangle[i + 1][j], dp[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i][j] + triangle[i + 1][j + 1], dp[i + 1][j + 1])
    return max(dp[-1])