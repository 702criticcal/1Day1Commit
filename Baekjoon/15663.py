from itertools import permutations

n, m = map(int, input().split())
nLst = list(map(int, input().split()))

for permu in sorted(list(set(permutations(nLst, m)))):
    print(*permu)
