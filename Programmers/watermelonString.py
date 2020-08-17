def solution(n):
    answer = ''
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer = answer + "박"
        else:
            answer = answer + "수"
    return answer

# 수박 문자열을 n만큼 만들어놓고 n자리까지 자르기
def solution(n):
    s = "수박" * n
    return s[:n]