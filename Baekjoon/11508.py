N = int(input())
C = sorted([int(input()) for _ in range(N)], reverse=True)
res = 0

for i in range(N):
    if i % 3 != 2:
        res += C[i]
print(res)
