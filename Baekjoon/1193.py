num = int(input())

for i in range(0, num):
    if i < num:
        num -= i
        continue
    break

if (i % 2) != 0:
    print(f'{i - (num - 1)}/{1 + (num - 1)}')
else:
    print(f'{1 + (num - 1)}/{i - (num - 1)}')
