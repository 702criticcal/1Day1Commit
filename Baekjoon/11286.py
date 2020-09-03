# 1차 시도. 시간 초과 실패.
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, [abs(x), x])
    else:
        if heap:
            result = heapq.heappop(heap)
            print(result[1])
        else:
            print(0)

# 2차 시도. 성공. input()이 느리긴 확실히 많이 느리다...ㅠ
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, [abs(x), x])
    else:
        if heap:
            result = heapq.heappop(heap)
            print(result[1])
        else:
            print(0)
