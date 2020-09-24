# 유클리드 호제법을 이용하여 최대공약수와 최대공배수 계산.
def solution(arr):
    answer = arr[0]

    def gcd(a, b):
        x = max(a, b)
        y = min(a, b)
        while y > 0:
            x, y = y, x % y
        return x

    for i in range(1, len(arr)):
        answer = arr[i] * answer // gcd(answer, arr[i])
    return answer