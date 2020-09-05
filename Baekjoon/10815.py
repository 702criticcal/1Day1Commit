# 1차 시도. 시간 초과 실패. 반복문 길이가 너무 길어서 시간 초과가 나는 것 같다.
import sys

N = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))

for i in checkList:
    if i in cardList:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 2차 시도. 성공. 이분 탐색을 익혀 반복문의 시간을 크게 줄였더니 성공할 수 있었다.
import sys

def binarySearch(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))
cardList.sort()
M = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))

for i in checkList:
    print(binarySearch(i, cardList), end=' ')
