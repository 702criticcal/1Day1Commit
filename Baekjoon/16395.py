def factorial(num):
    if num <= 1:
        return 1
    if dp[num]:
        return dp[num]
    else:
        dp[num] = num * factorial(num - 1)
        return num * factorial(num - 1)


n, k = map(int, input().split())
dp = [0] * 31
print(factorial(n - 1) // (factorial(k - 1) * factorial(n - k)))
