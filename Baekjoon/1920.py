import sys


def binary_search(target, lst):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == lst[mid]:
            return 1
        elif target > lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
targetlst = list(map(int, sys.stdin.readline().split()))

for i in targetlst:
    print(binary_search(i, A))
