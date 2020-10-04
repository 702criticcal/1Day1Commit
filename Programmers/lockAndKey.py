# 자물쇠가 키로 열리는지 체크하는 함수 check.
def check(x, y, key, lock, expandSize, start, end):
    # 자물쇠 주변으로 열쇠를 넣을 수 있는 공간을 만들어 큰 리스트를 만들어서 풀이한다.
    expandLock = [[0] * expandSize for _ in range(expandSize)]

    # 확장한 자물쇠 리스트에 정해진 x, y값부터 키 값을 추가한다.
    for i in range(len(key)):
        for j in range(len(key)):
            expandLock[x + i][y + j] += key[i][j]

    # 확장한 자물쇠 리스트에 자물쇠가 들어갈 자리에 자물쇠 값을 추가하여 자물쇠가 열리는지 판단한다.
    for i in range(start, end):
        for j in range(start, end):
            expandLock[i][j] += lock[i - start][j - start]
            # 0인 값이 있으면 열리지 않는 부분이 있다는 뜻이므로 더이상 돌리지 않고 False를 리턴한다.
            if expandLock[i][j] != 1:
                return False
    return True

# 2차원 리스트를 90 회전하는 함수 rotate_90.
def rotate_90(matrix):
    N = len(matrix)
    ret = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[j][N - 1 - i] = matrix[i][j]
    return ret


def solution(key, lock):
    start = len(key) - 1 # 확장한 자물쇠 리스트에서 진짜 자물쇠가 시작할 위치.
    end = start + len(lock) # 확장한 자물쇠 리스트에서 진짜 자물쇠가 끝날 위치.
    expandSize = start * 2 + len(lock) # 확장한 자물쇠 리스트의 길이.

    # 90도씩 4번 회전하여 모든 경우를 확인한다.
    for _ in range(4):
        # (0, 0)부터 자물쇠에 걸치는 마지막 부분인 (end, end)까지 반복하여 check 함수를 확인한다.
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expandSize, start, end):
                    return True
        key = rotate_90(key)
    return False