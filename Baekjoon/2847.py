N = int(input())
grade = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N - 1, 0, -1):
    if grade[i] > grade[i - 1]:
        continue
    else:
        cnt += grade[i - 1] - grade[i] + 1
        grade[i - 1] = grade[i] - 1
print(cnt)
