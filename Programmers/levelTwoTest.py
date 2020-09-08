# 1번 문제. 주어진 숫자가 몇 개 조합의 연속된 숫자의 합으로 표현될 수 있는지 계산하는 문제.
# 테스트 케이스 최대 숫자가 10,000이라 완전 탐색으로 간단히 구현했는데도 실행 시간이 느리지 않았다.
# 연속된 숫자의 합으로 표현될 수 있으면 cnt += 1, 연속된 숫자의 합이 n을 넘으면 다음 숫자로 넘어가는 방식을 1부터 n까지 반복하는 것으로 구현했다.
def solution(n):
    cnt = 1

    for i in range(1, n + 1):
        check = i
        for j in range(i + 1, n + 1):
            if check == n:
                cnt += 1
            elif check > n:
                break
            check += j

    return cnt


# 2번 문제. 종이 조각으로 만들 수 있는 모든 경우의 수에서 소수가 몇 개 인지 찾는 문제.
# 에라토스테네스의 체를 사용하여 풀었는데 빠르게 해결하느라 따로 체를 만들어서 풀었기 때문에 더 느렸을거다.
# made_nums 조합에서 바로 구할 수 있으면 좋았을텐데.. 적는 도중 방법이 생각났다.
from itertools import permutations

def solution(numbers):
    cnt = 0
    made_nums = []
    for i in range(1, len(numbers) + 1):
        made_nums += map(int, (map(''.join, permutations(numbers, i))))
    made_nums = set(made_nums)
    biggest = max(made_nums)

    check = [False, False] + [True] * (biggest - 1)

    for i in range(int(biggest ** 0.5)):
        if check[i] == True:
            for j in range(2 * i, biggest + 1, i):
                if check[j] == True:
                    check[j] = False

    for num in made_nums:
        if check[num] == True:
            cnt += 1
    return cnt

# 간단하게 체를 없애보았다. made_nums에서 해당 수가 소수인지 바로 판별하여 소수일 경우 cnt += 1을 해주었다. 왜 이게 생각이 안났지...
from itertools import permutations

def solution(numbers):
    cnt = 0
    made_nums = []
    for i in range(1, len(numbers) + 1):
        made_nums += map(int, (map(''.join, permutations(numbers, i))))
    made_nums = set(made_nums)

    for num in made_nums:
        isPrime = True
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            cnt += 1
    return cnt