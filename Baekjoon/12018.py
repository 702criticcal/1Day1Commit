# 1차 시도. 성공. 파이썬 heapq 모듈의 nlargest 메소드를 이용하여 해결했다!
import sys
import heapq

sungjoon = []
subject = 0
count = 0

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    P, L = map(int, sys.stdin.readline().split())
    mileage = list(map(int, sys.stdin.readline().split()))
    if P < L:
        heapq.heappush(sungjoon, 1)
    else:
        heapq.heapify(mileage)
        heapq.heappush(sungjoon, heapq.nlargest(L, mileage)[-1])

for i in range(n):
    if subject <= m:
        subject += heapq.heappop(sungjoon)
        if subject > m:
            break
        count += 1
print(count)
