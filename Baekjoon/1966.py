import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    N, M = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while queue:
        if M != 0:
            if max(queue) > queue[0]:
                first = queue.popleft()
                queue.append(first)
            else:
                queue.popleft()
                cnt += 1
            M -= 1
        else:
            if max(queue) > queue[0]:
                first = queue.popleft()
                queue.append(first)
                M = len(queue) - 1
            else:
                cnt += 1
                break
    print(cnt)
