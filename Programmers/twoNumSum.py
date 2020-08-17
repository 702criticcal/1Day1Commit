def solution(a, b):
    a = int(a)
    b = int(b)
    answerList = []
    if a > b:
        for i in range(b, a + 1):
            answerList.append(i)
        return sum(answerList)
    elif b > a:
        for i in range(a, b + 1):
            answerList.append(i)
        return sum(answerList)
    else:
        return a