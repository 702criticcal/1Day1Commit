import sys

stack = []

for _ in range(0, int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        stack.append(int(command[1]))
