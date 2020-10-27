import sys

input = sys.stdin.readline

N = int(input())
Xs = list(map(int, input().split()))
idxs = sorted(list(set(Xs)))

res = {}
for i in range(len(idxs)):
    res[idxs[i]] = i
for i in Xs:
    print(res[i], end=' ')
