import sys
import heapq

n = int(sys.stdin.readline())
present = []

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 0:
        if present:
            print(-heapq.heappop(present))
        else:
            print(-1)
    else:
        for value in a[1:]:
            heapq.heappush(present, -value)
