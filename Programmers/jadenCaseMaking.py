# 문제가 개편되지 않았을 때는, 공백이 무조건 하나여서 title()로 풀 수 있었지만,
# 지금은 공백이 여러개가 겹쳐서 주어지는 테스트케이스가 생겨 title()로는 풀리지 않습니다.
def solution(s):
    answer = ''
    lowerS = s.lower() # 대소문자가 섞인 문자열을 소문자로만 구성되게 전처리.
    idx = 0 # 단어의 첫 문자임을 표시하는 인덱스 변수.
    for i in range(len(lowerS)):
        # 공백이라면 결과값에 공백을 추가하고, idx를 0으로 초기화한다.
        if lowerS[i] == ' ':
            answer += ' '
            idx = 0
        else:
            # 문자이고, 단어의 첫문자라면 대문자로 바꾼 후 결과값에 추가한다.
            if idx == 0 and lowerS[i].isalpha():
                answer += lowerS[i].upper()
            # 첫문자가 아니라면 그대로 결과값에 추가한다.
            else:
                answer += lowerS[i]
            idx += 1
    return answer