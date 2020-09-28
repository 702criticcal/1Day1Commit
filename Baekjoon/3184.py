import sys

sys.setrecursionlimit(100000)


def dfs(yard, i, j, R, C):
    global sheep_cnt
    global wolf_cnt
    if i < 0 or i >= R or j < 0 or j >= C or yard[i][j] == '#':
        return sheep_cnt, wolf_cnt

    if yard[i][j] == 'o':
        sheep_cnt += 1
    elif yard[i][j] == 'v':
        wolf_cnt += 1
    yard[i][j] = '#'

    dfs(yard, i + 1, j, R, C)
    dfs(yard, i - 1, j, R, C)
    dfs(yard, i, j + 1, R, C)
    dfs(yard, i, j - 1, R, C)

    return sheep_cnt, wolf_cnt


R, C = map(int, input().split())
yard = [list(input()) for _ in range(R)]
sheep_answer = 0
wolf_answer = 0

for i in range(R):
    for j in range(C):
        sheep_cnt = 0
        wolf_cnt = 0
        if yard[i][j] != '#':
            sheep_cnt, wolf_cnt = map(int, dfs(yard, i, j, R, C))
            # 양이 늑대보다 많다면 늑대를 쫓아내고, 늑대가 더 많거나 같다면 양을 잡아먹는다.
            if wolf_cnt >= sheep_cnt:
                sheep_cnt = 0
            else:
                wolf_cnt = 0
            sheep_answer += sheep_cnt
            wolf_answer += wolf_cnt

print(sheep_answer, wolf_answer)
