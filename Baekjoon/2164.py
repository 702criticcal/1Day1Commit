import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N + 1)])

while queue:
    dumpCard = queue.popleft()
    if queue:
        secondCard = queue.popleft()
        queue.append(secondCard)
    else:
        print(dumpCard)
        break
