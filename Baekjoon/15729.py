N = int(input())
goal = list(map(int, input().split()))
btns = [0] * N
cnt = 0

for i in range(N):
    if i != N - 2 and i != N - 1 and btns[i] != goal[i]:
        btns[i] = 1 if btns[i] == 0 else 0
        btns[i + 1] = 1 if btns[i + 1] == 0 else 0
        btns[i + 2] = 1 if btns[i + 2] == 0 else 0
        cnt += 1
    if i == N - 2 and btns[i] != goal[i]:
        btns[i] = 1 if btns[i] == 0 else 0
        btns[i + 1] = 1 if btns[i + 1] == 0 else 0
        cnt += 1
    if i == N - 1 and btns[i] != goal[i]:
        btns[i] = 1 if btns[i] == 0 else 0
        cnt += 1
print(cnt)
