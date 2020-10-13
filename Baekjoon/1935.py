N = int(input())
formula = list(input())
vars = {}
for i in range(N):
    vars[chr(65 + i)] = int(input())

stack = [vars[formula.pop(0)]]

while formula:
    if formula[0] in vars:
        stack.append(vars[formula.pop(0)])
    else:
        b = stack.pop()
        a = stack.pop()
        if formula[0] == '+':
            stack.append(a + b)
        elif formula[0] == '-':
            stack.append(a - b)
        elif formula[0] == '*':
            stack.append(a * b)
        elif formula[0] == '/' and b != 0:
            stack.append(a / b)
        formula.pop(0)
print("%.2f" % stack[-1])
