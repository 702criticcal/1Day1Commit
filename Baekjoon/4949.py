while True:
    stack = []
    str = list(input())
    if len(str) == 1 and str[0] == '.':
        break
    for i in str:
        if i == '[' or i == ']':
            stack.append(i)
            if len(stack) >= 2:
                if stack[-2] == '[' and stack[-1] == ']':
                    stack.pop()
                    stack.pop()
        elif i == '(' or i == ')':
            stack.append(i)
            if len(stack) >= 2:
                if stack[-2] == '(' and stack[-1] == ')':
                    stack.pop()
                    stack.pop()
        else:
            continue
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
