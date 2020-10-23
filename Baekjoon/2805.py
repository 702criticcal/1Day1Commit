import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))


def sum(h):
    takeTree = 0

    for i in trees:
        if i - h > 0:
            takeTree += i - h

    return takeTree


def binarySearch(target):
    start, end = 0, max(trees)
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        takeTree = sum(mid)

        if takeTree < M:
            end = mid - 1
        elif takeTree >= M:
            ans = mid
            start = mid + 1
    return ans


print(binarySearch(M))