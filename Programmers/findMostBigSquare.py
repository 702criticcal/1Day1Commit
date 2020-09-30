def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                # 길이기 2가 넘는 정사각형이려면 최소 왼쪽, 위, 왼쪽 위 대각선의 요소가 1이어야 된다.
                # 하나 하나 확인하면서 사각형을 넓혀간다.
                # 최솟값인 이유는 셋 중 0이 하나라도 껴있을 경우엔 사각형이 아니므로 길이가 2 이상인 사각형이 아니게 된다.
                # 1이 최솟값인 경우, 2, 3, 4, ... 모든 경우에도 만족한다.
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
    return max([max(i) for i in board]) ** 2