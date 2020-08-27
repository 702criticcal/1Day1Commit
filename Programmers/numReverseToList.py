# 1차
def solution(n):
    nList = list(str(n))
    nList.reverse()
    return list(map(int,nList))

# 2차 - 코드 간소화
def solution(n):
    return list(map(int,reversed(str(n))))
