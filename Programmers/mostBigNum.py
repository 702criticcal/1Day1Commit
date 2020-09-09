# 1차 시도. 시간 초과 실패. 순열을 이용한 완전 탐색으로 풀었는데 하나도 빠짐없이 시간 초과 실패했다.
from itertools import permutations

def solution(numbers):
    return str(max(list(map(''.join, permutations(list(map(str,numbers)))))))

# 2차 시도. 90.9점 실패.
def solution(numbers):
    return ''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))

# 3차 시도. 성공. 중복되는 0을 하나의 0으로 줄여주기 위해 int형으로의 변환을 거치고 다시 str형으로 리턴한다.
def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: (x*3), reverse=True))))