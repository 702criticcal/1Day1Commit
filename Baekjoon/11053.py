import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        # i 보다 앞에 있는 요소와 비교하여 작은 수의 개수만큼 갑을 변경해준다.
        if A[j] < A[i]:
            # 자기 자신과 자신보다 앞에 있는 수 중 가장 큰 길이에 1을 더한 것을 비교하여 값을 변경한다.
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
