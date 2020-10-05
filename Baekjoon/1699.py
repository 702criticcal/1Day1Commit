n = int(input())
dp = [0 for _ in range(n + 1)]
# 제곱수를 저장하는 리스트.
square = [i * i for i in range(1, 317)]

for i in range(1, n + 1):
    temp = n
    for j in square:
        # i 보다 작은 제곱수에 대해 모두 결과값을 구하고 비교하여 최솟값을 구한다.
        if i < j:
            break
        temp = min(temp, dp[i - j])
    dp[i] = temp + 1
print(dp[n])
