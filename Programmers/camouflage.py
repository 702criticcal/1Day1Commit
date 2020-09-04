# 이 문제를 통해 Counter, reduce, lambda 함수에 대해 다시 공부하게 됐다.. 더 열심히 하자!
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter(kind for name, kind in clothes)
    return reduce(lambda x, y : x * (y + 1), cnt.values(), 1) - 1

def solution(clothes):
    return reduce(lambda x, y: x * y, [i + 1 for i in Counter([c[1] for c in clothes]).values()], 1) - 1