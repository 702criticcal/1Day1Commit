# 1차 시도. 메모리 초과 실패.
MAX_NUM = 10000

inputList = []

for _ in range(int(input())):
    inputList.append(int(input()))

N = len(inputList)

countList = [0] * (MAX_NUM + 1)
countSumList = [0] * (MAX_NUM + 1)

for i in range(N):
    countList[inputList[i]] += 1

countSumList[0] = countList[0]
for i in range(1, MAX_NUM + 1):
    countSumList[i] = countSumList[i - 1] + countList[i]

sortedList = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    sortedList[countSumList[inputList[i]]] = inputList[i]
    countSumList[inputList[i]] -= 1

for i in sortedList[1:]:
    print(i)


# 2차 시도. 메모리 초과 실패. countSumList를 없애보았지만 또 메모리 초과..
MAX_NUM = 10000

inputList = []

for _ in range(int(input())):
    inputList.append(int(input()))

N = len(inputList)

countList = [0] * (MAX_NUM + 1)

for i in range(N):
    countList[inputList[i]] += 1

for i in range(1, MAX_NUM + 1):
    countList[i] += countList[i - 1]

sortedList = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    sortedList[countList[inputList[i]]] = inputList[i]
    countList[inputList[i]] -= 1

for i in sortedList[1:]:
    print(i)


# 3차 시도. 메모리 초과 시도. input() 대신 sys.stdin.readline()을 사용하여 메모리를 줄여봤지만 역시 메모리 초과...
import sys

inputList = []

for _ in range(int(sys.stdin.readline())):
    inputList.append(int(sys.stdin.readline()))

countList = [0] * 10001
countSumList = [0] * 10001

for i in range(len(inputList)):
    countList[inputList[i]] += 1

countSumList[0] = countList[0]
for i in range(1, 10001):
    countSumList[i] = countSumList[i - 1] + countList[i]

sortedList = [0] * (len(inputList) + 1)

for i in range(len(inputList) - 1, -1, -1):
    sortedList[countSumList[inputList[i]]] = inputList[i]
    countSumList[inputList[i]] -= 1

for i in sortedList[1:]:
    print(i)


# 4차 시도. 성공. 길이 10001인 리스트를 2개 혹은 3개를 사용하던 것이 문제인 것 같아 입력받을 때 바로 count하는 것으로 코드를 수정하였다.
# 또한, 결과 출력 리스트 대신 countList에서 값 만큼 수를 출력해주는 것으로 수정했더니 성공했다!
# 메모리를 최대한 줄이려고 애썼다...
import sys

countList = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    countList[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if countList[i] != 0:
        for j in range(countList[i]):
            print(i)
