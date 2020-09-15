# (0, 0), (0, M -1), (N -1, 0), (N - 1, M - 1)은 값을 바꿀 수 있는 횟수가 딱 한번 뿐이다.
# 그렇기 때문에 (0, 0)부터 진행한다고 하면 (0, 1)도 값이 바뀌는데 이 상황에서 (0, 1)이 다르다면
# (0, 1)도 (0, 1)에서밖에 값을 바꿀 수 없다. 그래서 결국 처음부터 끝까지 다를 경우 계속 반복하면서 풀이해야 한다.
N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]


def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]


cnt = 0
for i in range(0, N - 2):
    for j in range(0, M - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)
