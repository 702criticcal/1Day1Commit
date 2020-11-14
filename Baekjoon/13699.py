def calc():
    res = 0
    for i in range(len(dp)):
        res += dp[i] * dp[len(dp) - i - 1]
    return res


if __name__ == "__main__":
    n = int(input())
    dp = [1]
    for i in range(n):
        dp.append(calc())
    print(dp[n])
