import sys

input = sys.stdin.readline

N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    # N + 1일째에 퇴사하므로 N보다 크면 상담을 완료할 수 없음.
    if i + tasks[i][0] <= N:
        dp[i] = tasks[i][1]
        # i에서 i보다 작은 것중에 더 많은 금액을 주는 상담이 있으면 값 변경.
        for j in range(i):
            if j + tasks[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + tasks[i][1])

print(max(dp))
