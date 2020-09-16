def solution(s):
    s_lst = list(s)
    stack = []

    for bracket in s_lst:
        stack.append(bracket)
        if len(stack) >= 2 and stack[-2:] == ['(', ')']:
            stack.pop()
            stack.pop()

    return not bool(stack)