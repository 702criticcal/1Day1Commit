def operate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2


for _ in range(int(input())):
    expression = input().split()
    res = operate(int(expression[0]), expression[1], int(expression[2]))
    print("correct" if res == int(expression[4]) else "wrong answer")
