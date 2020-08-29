from collections import deque
import sys

queue = deque([])

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif command[0] == 'size':
        print(len(queue))
    else:
        queue.append(command[1])
