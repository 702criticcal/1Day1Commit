import sys
import heapq

score = 0
N = int(sys.stdin.readline())
slime = list(map(int, sys.stdin.readline().split()))
heapq.heapify(slime)

while len(slime) > 1:
    x = heapq.heappop(slime)
    y = heapq.heappop(slime)
    heapq.heappush(slime, x + y)
    score += x * y
print(score)
