# 모든 종이 조각 조합을 순열로 찾기 위해 itertools의 permutations 사용.
from itertools import permutations


def solution(numbers):
    cnt = 0
    # 모든 종이조각 조합을 저장할 made_nums 리스트.
    made_nums = []
    for i in range(1, len(numbers) + 1):
        made_nums += list(map(''.join, permutations(numbers, i)))
    # 중복을 배제하기 위해 set 사용.
    made_nums = set(map(int, made_nums))

    # 에라토스테네스의 체를 사용하여 소수 찾기.
    biggest = max(made_nums)
    check = [False, False] + [True] * (biggest - 1)
    primes = []

    # 소수 찾기.
    for i in range(2, biggest + 1):
        if check[i]:
            primes.append(i)
            for j in range(2 * i, biggest + 1, i):
                check[j] = False

    # 찾은 소수 리스트 안에 있는 수인지 확인하여 cnt 증가.
    for num in made_nums:
        if num in primes:
            cnt += 1
    return cnt

# 눈여겨 볼 풀이.
# 가능한 수를 a에 저장하고 에라토스테네스의 체로 a에서 제거하는 풀이.
from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        # 비트 연산자를 이용했다는 사실이 흥미로웠다.
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
