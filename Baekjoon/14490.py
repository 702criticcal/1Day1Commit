def gcd(a, b):
    x = max(a, b)
    y = min(a, b)

    while y:
        x, y = y, x % y
    return x


n, m = map(int, input().split(':'))
gcd = gcd(n, m)
print(str(n // gcd) + ':' + str(m // gcd))
