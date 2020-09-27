# 컴파일러구조 수업 시간에 정규표현식에 대해서 배우긴 했지만, 코딩으로 이렇게 구현할 수 있다는 것을 알게된 것은 처음이다.
# 앞으로 문자열 문제를 해결할 때 정규표현식을 사용하면 간편하게 해결할 수 있는 문제에 앞으로 적용하면 좋을 것 같다!
# 정규표현식을 사용하기 위한 Python 모듈 re.
import re


def solution(dartResult):
    # bonus, option 매핑.
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    # re 모듈을 이용한 정규표현식으로 문자열을 나눈다.
    # \d+ 는 숫자를 뜻하는 \d와 1개 이상을 뜻하는 +로 한 자리수 이상의 숫자를 뜻한다.
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    for i in range(len(dart)):
        # 스타상 당첨 시, 해당 점수 이외에도 바로 전에 얻은 점수를 2배로 만들어주어야 한다.
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        # 점수 계산.
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    return sum(dart)
