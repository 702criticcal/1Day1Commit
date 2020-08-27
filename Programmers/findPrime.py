# 에라토스테네스의 체 사용
def solution(n):
    sieve = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False
    return len([i for i in range(2, n + 1) if sieve[i]])

# 더 간결한 에라토스테네스의 체 코드 구현
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)