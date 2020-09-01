# 1차 시도. 성공.
inputList = [list(map(int, input().split())) for _ in range(int(input()))]
sortedList = sorted(inputList, key=lambda x: (x[1], x[0]))

for i, j in sortedList:
    print(i, j)
