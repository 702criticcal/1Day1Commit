import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    firstNote = sorted(list(map(int, input().split())))
    M = int(input())
    secondNote = list(map(int, input().split()))
    result = []

    for num in secondNote:
        start, end = 0, N - 1
        find = False

        while start <= end:
            mid = (start + end) // 2

            if num < firstNote[mid]:
                end = mid - 1
            elif num > firstNote[mid]:
                start = mid + 1
            else:
                find = True
                break

        if find:
            result.append(1)
        else:
            result.append(0)

    for res in result:
        print(res)
