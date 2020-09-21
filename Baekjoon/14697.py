# # 1차 시도. 실패.
# A, B, C, N = map(int, input().split())
# dp = [0] * (N + 1)
# dp[A] = dp[B] = dp[C] = 1
#
# for i in range(N + 1):
#     if dp[i] == 1 and (i + C) <= N:
#         dp[i + A] = 1
#         dp[i + B] = 1
#         dp[i + C] = 1
# print(dp[N])

# 2차 시도. 런타임 에러 실패.
A, B, C, N = map(int, input().split())
dp = [0] * (N + 1)
dp[A] = dp[B] = dp[C] = 1

for i in range(A, N + 1):
    for j in [A, B, C]:
        if i >= j and dp[i - j] == 1:
            dp[i] = 1
print(dp[N])


# 3차 시도. 성공.
A, B, C, N = map(int, input().split())
# N + 1에서 최대 크기인 301로 설정했더니 성공했는데, 300일 때의 차이가 무엇인지 잘 모르겠다..
dp = [0] * 301
dp[A] = dp[B] = dp[C] = 1

for i in range(A, N + 1):
    for j in [A, B, C]:
        if i >= j and dp[i - j] == 1:
            dp[i] = 1
print(dp[N])