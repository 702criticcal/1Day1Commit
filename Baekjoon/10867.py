N = int(input())
numList = sorted(list(set(list(map(int, input().split())))))
print(' '.join(list(map(str, numList))))