# 1차 시도. 시간 초과 실패. 실행 시간 계산 시, 3.XX 대
# 11651번과 시간 제한, 메모리 제한, 입력 크기도 똑같아서 같은 방식을 풀었는데 무엇이 문제일까..
inputList = [list(map(int, input().split())) for _ in range(int(input()))]
sortedList = sorted(inputList, key= lambda x: (x[0], x[1]))
for i, j in sortedList:
    print(i ,j)

# 2차 시도. 성공.
# time 모듈을 사용하여 시간을 계산해보았다. 실행 시간 계산 시, 2.XX 대
# 파이써닉 코드를 위해 for문을 range(int(input()))으로 작성했었는데 이게 실행 시간 상으로는 좋지 못하다는 사실을 알게 되었다!
import time
start = time.time()

N = int(input())

inputList = [list(map(int, input().split())) for _ in range(N)]
sortedList = sorted(inputList, key= lambda x: (x[0], x[1]))
for i, j in sortedList:
    print(i ,j)

print("time : ", time.time() - start)