def convert(n):
    result = ''
    while n > 0:
        n, m = divmod(n, 3)
        result += ['0', '1', '2'][m]
    return result[::-1]


def solution(n):
    answer = 0
    convert3 = convert(n)
    for i in range(len(convert3)):
        answer += int(convert3[i]) * (3 ** i)
    return answer
