def solution(n):
    divisorSum = n
    if n == 0:
        return 0
    else:
        for i in range(1, n//2 + 1):
            if n % i == 0:
                divisorSum += i
    return divisorSum

