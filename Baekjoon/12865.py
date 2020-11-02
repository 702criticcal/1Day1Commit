n, k = map(int, input().split())
items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append([w, v])
dp = [0 for _ in range(k + 1)]

for i in range(n):
    for j in range(k, 0 , -1):
        # 해당 짐이 가방의 용량보다 작으면,
        if items[i][0] <= j:
            # 그 용량의 가치 최댓값을 현재의 가치값과 그 짐을 포함하기 전 용량의 가치 최댓값과 짐의 가치를 더한 값 중 최댓값으로 설정한다.
            dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])

print(dp[k])
