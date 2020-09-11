# 1차 시도. 실패.
def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    while True:
        if x % y == 0:
            return y
        else:
            return gcd(x, x % y)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(int(A * B / gcd(A, B)))


# 2차 시도. 성공.
def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    while y:
        x, y = y, x % y
    return x


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))