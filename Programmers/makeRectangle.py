from collections import Counter

def solution(v):
    answer = []
    Xs = Counter([i[0] for i in v])
    Ys = Counter([i[1] for i in v])

    for x in Xs:
        if Xs[x] == 1:
            answer.append(x)
    for y in Ys:
        if Ys[y] == 1:
            answer.append(y)

    return answer