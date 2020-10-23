from copy import deepcopy


# 연산 수행하는 메소드 operate.
def operate(n, m, op):
    if op == '+':
        return n + m
    elif op == '-':
        return n - m
    elif op == '*':
        return n * m


def solution(expression):
    answer = 0 # 각 경우마다 최댓값을 저장할 변수.
    # 연산의 우선순위가 총 3! = 6가지가 나올 수 있으므로 해당 우선순위를 미리 리스트로 구현해준다.
    operatorPriority = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+'], ['*', '-', '+'],
                        ['*', '+', '-']]
    # 문자열에서 숫자를 뽑아낸다.
    numLst = list(map(int, expression.replace('+', ' ').replace('*', ' ').replace('-', ' ').split()))
    # 문자열에서 연산자를 뽑아낸다.
    operatorLst = [i for i in expression if not i.isdigit()]

    # 6 가지의 연산자 우선 순위만큼 반복하여 최댓값을 구한다.
    for prior in operatorPriority:
        # 리스트를 총 6 번 반복해서 사용해야 하므로 deepcopy를 통해 수정해도 원본은 남아 있게 해준다.
        tempNumLst = deepcopy(numLst)
        tempOperatorLst = deepcopy(operatorLst)

        # 각 경우의 연산자 우선 순위 순서대로 연산을 진행한다.
        for p in prior:
            i = 0
            while tempOperatorLst:
                if i >= len(tempOperatorLst):
                    break
                if tempOperatorLst[i] == p:
                    temp = operate(tempNumLst[i], tempNumLst[i + 1], p)
                    tempNumLst.pop(i)
                    tempNumLst.pop(i)
                    tempNumLst.insert(i, temp)
                    tempOperatorLst.pop(i)
                else:
                    i += 1
        # 현재까지의 최댓값과 현재 값의 절댓값을 비교하여 최댓값을 최신화한다.
        answer = max(answer, abs(tempNumLst[0]))
    return answer
