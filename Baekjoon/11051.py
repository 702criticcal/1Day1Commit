import sys

sys.setrecursionlimit(100000)

def factorial(num):
    if num <= 1:
        return 1
    if dp[num]:
        return dp[num]
    else:
        dp[num] = num * factorial(num - 1)
        return dp[num]


if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [0] * (n + 1)

    print((factorial(n) // (factorial(k) * factorial(n - k))) % 10007)



from math import factorial

if __name__ == "__main__":
    n, k = map(int, input().split())

    print((factorial(n) // (factorial(k) * factorial(n - k))) % 10007)