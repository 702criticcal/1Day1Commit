# 내 코드. 에러가 나는데 문제를 결국 못찾고 정답 코드를 참고했다.
# 둘의 차이가 무엇인지 도대체 찾을 수가 없었다...
def solution(msg):
    answer = []
    d = {chr(i + 64): i for i in range(1, 27)}
    idx = 27

    while msg:
        # 이 부분만 구현 방법이 다른데 내 방법만 몇 개의 테스트케이스를 통과하지 못한다.
        for i in range(1, len(msg) + 1):
            if msg[:i] not in d:
                temp = i - 1
                break
        answer.append(d[msg[:temp]])
        d[msg[:temp + 1]] = idx
        idx += 1
        msg = msg[temp:]
    return answer


# 정답 코드.
def solution(msg):
    answer = []
    d = {chr(i + 64): i for i in range(1, 27)}
    idx = 27

    while msg:
        temp = 1
        while msg[:temp] in d and temp <= len(msg):
            temp += 1
        temp -= 1
        answer.append(d[msg[:temp]])
        d[msg[:temp + 1]] = idx
        idx += 1
        msg = msg[temp:]

    return answer

print(solution("ABABABABABABABAB"))