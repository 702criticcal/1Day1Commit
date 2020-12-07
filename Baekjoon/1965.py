n = int(input())
boxes = list(map(int, input().split()))
dp = [0] * 1001

for b in boxes:
    dp[b] = max(dp[:b]) + 1

print(max(dp))
