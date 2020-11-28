# 1차 시도. 효율성 테스트케이스 3개 시간 초과 실패.
# 이전에 백준에서 풀었던 문제라 같은 방식으로 풀었지만 같은 방식으로 프로그래머스에서는 효율성 테스트를 합격하지 못했다.
# 리스트에 값을 추가하는 방법, 리스틑 만들어두고 값을 변경하는 방법 둘 다 효율성 테스트를 불합격했다.
def solution(n):
    dp = [0] * 60001
    dp[1] = 1;
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n] % 1000000007


# 2차 시도. 성공. 리스트 대신 변수만 3개를 사용하여 다이나믹 프로그래밍하였다.
def solution(n):
    dp1 = 1; dp2 = 2

    for _ in range(3, n + 1):
        dp = dp1 + dp2
        dp1, dp2 = dp2, dp

    return dp % 1000000007


# 2020.11.28 2차 풀이.
# 저번에 풀었을 때보다 변수를 하나 더 줄여서 풀었다!
def solution(n):
    dp1, dp2 = 1, 2

    for i in range(n - 2):
        dp1, dp2 = dp2, dp1 + dp2

    return dp2 % 1000000007