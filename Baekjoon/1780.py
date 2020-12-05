def check(paper, x, y, l, answer):
    num = paper[x][y]

    for i in range(x, x + l):
        for j in range(y, y + l):
            if paper[i][j] != num:
                check(paper, x, y, l // 3, answer)
                check(paper, x, y + l // 3, l // 3, answer)
                check(paper, x, y + (l // 3) * 2, l // 3, answer)
                check(paper, x + l // 3, y, l // 3, answer)
                check(paper, x + l // 3, y + l // 3, l // 3, answer)
                check(paper, x + l // 3, y + (l // 3) * 2, l // 3, answer)
                check(paper, x + (l // 3) * 2, y, l // 3, answer)
                check(paper, x + (l // 3) * 2, y + l // 3, l // 3, answer)
                check(paper, x + (l // 3) * 2, y + (l // 3) * 2, l // 3, answer)
                return

    if num == -1:
        answer[0] += 1
    elif num == 0:
        answer[1] += 1
    else:
        answer[2] += 1
    return


if __name__ == "__main__":
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    answer = [0, 0, 0]  # -1, 0, 1
    check(paper, 0, 0, n, answer)

    for i in range(3):
        print(answer[i])
