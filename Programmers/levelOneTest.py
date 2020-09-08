# 1번 문제. 주어진 숫자보다 작은 소수의 개수 찾기 문제.
# 에라토스테네스의 체를 사용하여 풀었다.
def solution(n):
    cnt = 0
    check = [False, False] + [True] * (n - 1)

    for i in range(n + 1):
        if check[i] == True:
            cnt += 1
            for j in range(2 * i, n + 1, i):
                if check[j] == True:
                    check[j] = False
    return cnt



# 2번 문제. 문자열 치환 문제.
# 첫 번째 풀이. 리스트로 바꿔서 시도했지만 실패.
def solution(s):
    s_lst = list(s.split())
    result = ''
    for i in s_lst:
        for j in range(len(i)):
            if j % 2 == 0:
                result += i[j].upper()
            else:
                result += i[j].lower()
            print(result)
        if i == s_lst[-1]:
            break
        result += ' '
    return result

# 두 번째 풀이. 리스트로 바꾸지 않고 주어진 문자열 내에서 바꾸도록 구현하여 성공.
def solution(s):
    answer = ''
    index = 0
    for i in s:
        if i == ' ':
            answer += ' '
            index = 0
        else:
            if index % 2 == 0:
                answer += i.upper()
                index += 1
            else:
                answer += i.lower()
                index += 1
    return answer
