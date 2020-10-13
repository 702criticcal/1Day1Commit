import sys

input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [str(i) for i in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

print(' '.join(baskets[1:]))
