def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    while y:
        x, y = y, x % y
    return x


a, b = map(int, input().split())
print(gcd(a, b))
print(a * b // gcd(a, b))
