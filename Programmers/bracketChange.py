# 문자열 w를 u, v로 나누기 위한 함수.
# 올바른 괄호 문자열이 아닌 균형잡힌 괄호 문자열은 (와 )의 개수만 같으면 된다.
# u는 더 이상 나눌 수 없어야 하므로 가장 먼저 (와 )의 개수가 똑같아지는 부분에서 자른다.
def divide(p):
    openB = 0
    closeB = 0

    for i in range(len(p)):
        if p[i] == '(':
            openB += 1
        else:
            closeB += 1
        if openB == closeB:
            return p[:i + 1], p[i + 1:]


# 올바른 괄호 문자열인지 확인하는 함수.
# 스택을 활용하여 확인했다.
def isBalanced(u):
    stack = []

    for i in u:
        stack.append(i)
        if len(stack) >= 2 and stack[-2:] == ['(', ')']:
            stack.pop()
            stack.pop()
    if stack:
        return False
    else:
        return True


# 과정대로 구현한 함수.
def solution(p):
    answer = ''
    # 1 번 과정
    if p == '':
        return ''
    # 2 번 과정
    u, v = divide(p)
    # 3 번 과정
    if isBalanced(u):
        return u + solution(v)
    # 4 번 과정
    else:
        # 4-1 번 과정
        answer = '('
        # 4-2 번 과정
        answer += solution(v)
        # 4-3 번 과정
        answer += ')'
        # 4-4 번 과정
        for b in u[1:len(u) - 1]:
            if b == '(':
                answer += ')'
            else:
                answer += '('
        # 4-5 번 과정
        return answer