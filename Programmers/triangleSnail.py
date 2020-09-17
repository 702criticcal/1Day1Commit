def solution(n):
    # while문을 진행하기 위한 조건함수.
    def isFull(matrix):
        for i in matrix:
            if 0 in i:
                return True
        return False

    answer = []
    matrix = []
    for i in range(1, n + 1):
        matrix.append([0] * i)

    start, end = 0, n
    num = 1
    while isFull(matrix):
        # 가장 왼쪽 빗변을 타고 세로로 진행하며 채우는 for문.
        for i in range(start, end):
            if matrix[i][start] == 0:
                matrix[i][start] = num
                num += 1
        # 왼쪽부터 오른쪽으로 진행하며 가장 아랫줄을 채우는 for문.
        for j in range(start + 1, end):
            if matrix[end - 1][j] == 0:
                matrix[end - 1][j] = num
                num += 1
        # 삼각형의 오른쪽 빗변을 채우는 for문.
        temp = start + 1
        for k in range(end - 2, start, -1):
            if matrix[k][end - 1 - temp] == 0:
                matrix[k][end - 1 - temp] = num
                num += 1
                temp += 1
        start += 1
        end -= 1

    for i in matrix:
        answer += i

    return answer