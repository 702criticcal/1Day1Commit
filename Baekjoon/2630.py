def check(x, y, n):
    global blue, white

    color = paper[x][y]  # 색을 비교하기 위해 첫 번째 칸의 색을 변수에 저장.

    # 해당 색종이의 크기만큼 돌면서 색이 모두 같은지 확인.
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색이 다른 것이 있다면,
            if color != paper[i][j]:
                # n//2 크기의 작은 색종이 4개로 쪼개어 재귀 호출.
                check(x, y, n // 2)
                check(x + n // 2, y, n // 2)
                check(x, y + n // 2, n // 2)
                check(x + n // 2, y + n // 2, n // 2)
                return

    # 색이 모두 같을 시, 색에 따라 개수 +1.
    if color == '0':
        white += 1
    else:
        blue += 1
    return


if __name__ == "__main__":
    N = int(input())
    paper = [list(input().split()) for _ in range(N)]
    white = 0  # 하얀색 색종이의 수
    blue = 0  # 파란색 색종이의 수

    check(0, 0, N)
    print(white)
    print(blue)
