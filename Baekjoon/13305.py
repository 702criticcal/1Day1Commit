import sys

input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
fees = list(map(int, input().split()))
min_fee = fees[0]
ans = 0

for i in range(N - 1):
    # 최소 비용 저장.
    if fees[i] < min_fee:
        min_fee = fees[i]
    # 비용 계산.
    ans += min_fee * roads[i]

print(ans)
