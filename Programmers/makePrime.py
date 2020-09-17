# 에라토스테네스의 체 사용 코드.
from itertools import combinations


def solution(nums):
    answer = 0
    num_lst = list(map(sum, combinations(nums, 3)))
    max_num = max(num_lst)
    sieve = [False, False] + [True] * (max_num - 1)

    for i in range(max_num // 2 + 1):
        if sieve[i] == True:
            for j in range(i * 2, max_num + 1, i):
                sieve[j] = False

    for n in num_lst:
        if sieve[n] == True:
            answer += 1

    return answer


from itertools import combinations


# 에라토스테네스의 체 미사용 코드. 숫자마자 소수 판별 실시.
def solution(nums):
    def isPrime(num):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return 0
        return 1

    answer = 0
    num_lst = list(map(sum, combinations(nums, 3)))

    for n in num_lst:
        answer += isPrime(n)

    return answer
