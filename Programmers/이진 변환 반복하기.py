def solution(s):
    answer = [0, 0]
    x = s

    while x != '1':
        xTemp = x.replace('0', '')
        answer[1] += len(x) - len(xTemp)
        x = bin(len(xTemp))[2:]
        answer[0] += 1

    return answer
