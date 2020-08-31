# 1차 시도. 런타임 에러.
mathExpression = input()
stack = []
for s in mathExpression:
    stack.append(s)
    if len(stack) >= 3 and stack[-1] in ['*', '/', '+', '-']:
        operator = stack.pop()
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(str(eval(num1 + operator + num2)))
print(stack[-1])

# 2차 시도. 실패.
mathExpression = input()
stack = []
for s in mathExpression:
    if s.isdigit():
        stack.append(int(s))
    else:
        if s == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
        elif s == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
        elif s == '*':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
        elif s == '/':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 / num2)
print(stack[-1])

# 3차 시도. 성공!
# Python의 나눗셈 연산자가 문제였던 것 같다. Python3에서는 정수끼리 나누어도 실수형으로 출력되기 때문!
mathExpression = input()
stack = []
for s in mathExpression:
    if s.isdigit():
        stack.append(int(s))
    else:
        if s == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
        elif s == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
        elif s == '*':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
        elif s == '/':
            num2 = stack.pop()
            num1 = stack.pop()
            if num1 % num2 == 0:
                stack.append(num1 // num2)
            else:
                stack.append(num1 / num2)
print(stack[-1])
