# 반복문을 활용한 다이나믹 프로그래밍. 29380KB 메모리 사용. 68ms 소요.
n = int(input())
res = [0, 1, 2]
for i in range(3, n + 1):
    res.append(res[i - 1] + res[i - 2])
print(res[n] % 10007)


# 재귀를 활용한 다이나믹 프로그래밍. 29584KB 메모리 사용. 64ms 소요.
# 둘 다 거의 비슷비슷하다..
import sys

sys.setrecursionlimit(100000)


def f_dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dp[n]:
        return dp[n]
    else:
        dp[n] = f_dp(n - 1) + f_dp(n - 2)
        return dp[n]


n = int(input())
dp = [0] * (n + 1)
print(f_dp(n) % 10007)
