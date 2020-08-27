# 에라토스테네스의 체 사용
N = int(input())

sieve = [False, False] + [True] * (N - 1)
for i in range(2, int(N ** 0.5)):
    if sieve[i]:
        for j in range(2 * i, N, i):
            sieve[j] = False
primes = [i for i in range(2, N+1) if sieve[i]]

while N != 1:
    for prime in primes:
        if N % prime == 0:
            print(prime)
            N /= prime
            break

