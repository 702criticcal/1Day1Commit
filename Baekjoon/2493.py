import sys

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
result = []

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            result.append(stack[-1][0] + 1)
            break
        stack.pop()
    if not stack:
        result.append(0)
    stack.append([i, tower[i]])

print(' '.join(map(str, result)))
