n = int(input())

mirror = [input() for _ in range(n)]
k = int(input())

if k == 1:
    for i in range(n):
        print(mirror[i])
elif k == 2:
    for i in range(n):
        print(mirror[i][::-1])
else:
    for i in range(n - 1, -1, -1):
        print(mirror[i])
