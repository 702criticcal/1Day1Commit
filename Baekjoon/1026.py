# 정렬 문제였는데 개인적으로 A의 최댓값과 B의 최솟값을 곱해주는 것이 가장 작다고 생각했기 때문에 최대 힙과 최소 힙으로 구현해보았다.
import sys
import heapq

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
heapA = []
B = list(map(int, sys.stdin.readline().split()))
result = 0

for num in A:
    heapq.heappush(heapA, -num)
heapq.heapify(B)

for i in range(N):
    result += -(heapq.heappop(heapA)) * heapq.heappop(B)
print(result)
