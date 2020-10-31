from itertools import combinations_with_replacement

N, M = map(int, input().split())
numLst = list(map(int, input().split()))
for cwr in sorted(list(map(sorted, combinations_with_replacement(numLst, M)))):
    print(*cwr)
