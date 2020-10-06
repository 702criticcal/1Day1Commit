import math

def solution(n, m):
    g = math.gcd(n, m)
    return [g, n * m // g]