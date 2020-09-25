def solution(n):
    cnt = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            cnt += 1
            n -= 1
    return cnt


# 눈여겨볼 만한 풀이. 나누지 않고 2진법에서 1의 개수를 세서 풀었다..
def solution(n):
    return bin(n).count('1')