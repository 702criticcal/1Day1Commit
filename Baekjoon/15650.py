from itertools import combinations

n, m = map(int, input().split())
for i in list(map(' '.join, combinations([str(i) for i in range(1, n + 1)], m))):
    print(i)
