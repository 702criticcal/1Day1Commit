def check(arr, x, y, n, answer):
    num = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != num:
                check(arr, x, y, n // 2, answer)
                check(arr, x + n // 2, y, n // 2, answer)
                check(arr, x, y + n // 2, n // 2, answer)
                check(arr, x + n // 2, y + n // 2, n // 2, answer)
                return

    if num == 0:
        answer[0] += 1
    else:
        answer[1] += 1
    return


def solution(arr):
    answer = [0, 0]
    check(arr, 0, 0, len(arr), answer)
    return answer
