from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N + 1)])
result = []

while queue:
    dumpCard = queue.popleft()
    result.append(dumpCard)
    if queue:
        secondCard = queue.popleft()
        queue.append(secondCard)

for i in result:
    print(i, end=' ')
