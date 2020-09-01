# 1차 시도. 실패.
# Python의 soted() 메소드가 안정 정렬이라고 해서 사용해봤더니 틀렸다. 병합 정렬을 써야 할 듯 싶다.
import sys

N = int(sys.stdin.readline())
inputList = [list(sys.stdin.readline().split()) for _ in range(N)]
sortedList = sorted(inputList, key=lambda x: x[0])

for age, name in sortedList:
    print(age, name)

# 2차 시도. 시간 초과 실패.
# 병합 정렬을 써도 실패다..
import sys
import time
start = time.time()

N = int(sys.stdin.readline())
inputList = [list(sys.stdin.readline().split()) for _ in range(N)]


def mergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0][0] <= right[0][0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


sortedList = mergeSort(inputList)

for age, name in sortedList:
    print(age, name)
print("time : ", time.time() - start)

# 3차 시도. 성공..
# 1차 시도 코드에서 key 형변환을 해주지 않아 틀린거였다... 파이썬은 문자열도 정렬이 가능한데 왜 안된걸까?
# 좀 더 공부가 필요하겠다...
import sys

N = int(sys.stdin.readline())
inputList = [list(sys.stdin.readline().split()) for _ in range(N)]
sortedList = sorted(inputList, key=lambda x: int(x[0]))

for age, name in sortedList:
    print(age, name)
