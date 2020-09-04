from collections import deque


def solution(board, moves):
    cnt = 0
    dolls = []
    for i in range(len(board[0])):
        dolls.append([b[i] for b in board[::-1] if b[i]])

    stack = []
    for i in moves:
        if dolls[i - 1]:
            if dolls[i - 1][-1]:
                stack.append(dolls[i - 1].pop())
                if len(stack) >= 2 and stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    cnt += 2
    return cnt