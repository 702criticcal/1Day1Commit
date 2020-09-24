# 1차 풀이.
def solution(n):
    mod_lst = [1, 2, 4]
    answer = []
    while n > 0:
        n, mod = divmod(n, 3)
        answer.append(mod_lst[mod - 1])
        if mod == 0:
            n -= 1

    return ''.join(list(map(str, reversed(answer))))

# 2차 풀이.
def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer = "124"[mod - 1] + answer
        if mod == 0:
            n -= 1

    return answer