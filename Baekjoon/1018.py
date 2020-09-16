N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
res = 64

for i in range(N - 7):
    for j in range(M - 7):
        cnt_W = 0
        cnt_B = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # x, y 좌표의 합이 짝수면 가장 왼쪽 위 값과 똑같은 값을 가져야 한다.
                if (x + y) % 2:
                    # 가장 왼쪽 위 값이 W인 경우에서 좌표의 합이 짝수인 경우.
                    if chess[x][y] != "W":
                        cnt_W += 1
                    # 가장 왼쪽 위 값이 B인 경우에서 좌표의 합이 짝수인 경우.
                    if chess[x][y] != "B":
                        cnt_B += 1
                else:
                    # 가장 왼쪽 위 값이 W인 경우에서 좌표의 합이 홀수인 경우. -> B
                    if chess[x][y] != "B":
                        cnt_W += 1
                    # 가장 왼쪽 위 값이 B인 경우에서 좌표의 합이 홀수인 경우. -> W
                    if chess[x][y] != "W":
                        cnt_B += 1
        res = min(res, cnt_W, cnt_B)

print(res)
