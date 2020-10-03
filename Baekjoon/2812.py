N, K = map(int, input().split())
number = input()
stack = []

for i, num in enumerate(number):
    while len(stack) > 0 and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
        if K == 0:
            stack += number[i:]
            break
    if K == 0:
        break
    stack.append(number[i])
if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack[:]))
