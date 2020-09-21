import sys

input = sys.stdin.readline

N = int(input())
tips = sorted([int(input()) for _ in range(N)], reverse=True)
res = 0

for i in range(N):
    if i < tips[i]:
        res += tips[i] - i

print(res)
