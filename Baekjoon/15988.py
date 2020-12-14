if __name__ == "__main__":
    dp = [0 for _ in range(1000001)]

    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, 1000001):
        dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

    for _ in range(int(input())):
        n = int(input())
        print(dp[n] % 1000000009)
