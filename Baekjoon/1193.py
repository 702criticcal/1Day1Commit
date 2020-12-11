x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    print(f'{x}/{line - x + 1}')
else:
    print(f'{line - x + 1}/{x}')
