# 1차 시도. 성공. 최소 힙을 사용하여 구현하니 빠르게 잘 됐다!
import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cardList)

for _ in range(m):
    smallest = heapq.heappop(cardList)
    secondSmall = heapq.heappop(cardList)
    heapq.heappush(cardList, smallest + secondSmall)
    heapq.heappush(cardList, smallest + secondSmall)
print(sum(cardList))
