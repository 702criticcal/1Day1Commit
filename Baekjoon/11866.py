from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N + 1)])
result = []

while queue:
    for _ in range(K - 1):
        first = queue.popleft()
        queue.append(first)
    result.append(queue.popleft())
print('<' + ', '.join(list(map(str, result))) + '>')
