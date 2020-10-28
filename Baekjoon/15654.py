from itertools import permutations

N, M = map(int, input().split())
numLst = list(map(int, input().split()))

for c in sorted(list(permutations(numLst, M))):
    print(*c)
