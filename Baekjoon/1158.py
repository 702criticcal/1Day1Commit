from collections import deque

N, K = list(map(int, input().split()))

queue = deque([i for i in range(1, N + 1)])
result = []

while queue:
    for _ in range(K - 1):
        first = queue.popleft()
        queue.append(first)
    result.append(queue.popleft())
print('<' + ', '.join(list(map(str, result))) + '>')
