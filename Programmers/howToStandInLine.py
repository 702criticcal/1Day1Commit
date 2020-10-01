# n = 3일 때, 뒤의 두 자리를 정하는 경우의 수는 맨 앞 수가 1, 2, 3일 때 각각 2 씩이다.
# 경우의 수가 (n - 1)!라는 것이다. 그것은 모든 자리에서 만족하므로 모든 자리마다 각각 해당 수가 들어갈 수를 구해주면 된다.
# 모든 순열을 구하여 k 번째 방법을 구하는 것은 시간 초과가 나기 때문에 이 방법으로 풀어야 한다.
from math import factorial

def solution(n, k):
    answer = []
    num_lst = [i for i in range(1, n + 1)]

    while n > 0:
        fact = factorial(n - 1)
        answer.append(num_lst.pop((k - 1) // fact))
        n -= 1
        k %= fact

    return answer