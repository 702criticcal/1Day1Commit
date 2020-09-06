import sys
from itertools import permutations

N = int(sys.stdin.readline())
nList = [str(i) for i in range(1, N + 1)]
results = list(permutations(nList))

for permu in results:
    print(' '.join(permu))
