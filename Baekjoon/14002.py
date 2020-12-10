n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
answer = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j] + 1, dp[i])

order = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == order:
        answer.append(a[i])
        order -= 1

print(max(dp))
answer.reverse()
for i in answer:
    print(i, end=' ')
