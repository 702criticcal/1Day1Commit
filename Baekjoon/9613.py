def gcd(a, b):
    x = max(a, b)
    y = min(a, b)

    while y:
        x, y = y, x % y
    return x


t = int(input())
for _ in range(t):
    num_lst = list(map(int, input().split()))
    n = num_lst[0]
    ans = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            ans += gcd(num_lst[i], num_lst[j])
    print(ans)
