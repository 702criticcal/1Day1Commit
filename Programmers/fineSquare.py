# 1차 시도. 83.3점 실패.
# 일차 함수식을 이용해 봤는데 시간 초과 2개와 틀렸습니다 1개가 나왔다.
# 내가 생각하는 시간 복잡도 : O(n)
# 이유 : for문이 하나라서. 근데 w의 길이가 너무 길어서 시간초과가 난 것 같다.
def solution(w,h):
    answer = 0
    for x in range(1, w):
        answer += int((h / w) * x)
    return answer * 2

# 2차 시도. 38.9점 실패.
# 둘의 최대공약수를 이용해서 for문으로 돌리는 사각형 크기를 줄여봤는데 잘못됐나 보다.
def solution(w, h):
    answer = 0
    number = max(w, h)
    divisor = min(w, h)

    while (number % divisor) != 0:
        remainder = number % divisor
        number = divisor
        divisor = remainder

    smallw = w // divisor

    for x in range(1, smallw + 1):
        answer += int((h / w) * x)

    return w * h - answer * divisor

# 3차 시도. 94.4점 실패. 테스트 케이스 1 개가 시간초과가 났다..
# 2차 시도 때 빼줘야 할 사각형을 잘못 계산해서 그것을 고쳐주었다.
# 내가 생각하는 시간 복잡도 : O(n)
# 이유 : 이중 반복문이 없기 때문. 반복 횟수를 크게 줄였다고 생각했는데도 시간 초과가 난다..
def solution(w, h):
    number = max(w, h)
    divisor = min(w, h)

    while (number % divisor) != 0:
        remainder = number % divisor
        number = divisor
        divisor = remainder

    smallw = w // divisor
    smallSquare = smallw * (h // divisor)

    for x in range(1, smallw):
        smallSquare -= int((h / w) * x) * 2

    return w * h - smallSquare * divisor

# 4차 시도. 성공. 성능 차이도 확연하게 나고, 길이도 줄었다.
# 찾아보니 math 모듈에 gcd 함수가 있었고, ((w // gcd) + (h // gcd) - 1) * gcd 식을 통해 풀게 됐다.
from math import gcd

def solution(w,h):
    return w * h - (w + h - gcd(w,h))