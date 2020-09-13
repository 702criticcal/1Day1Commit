N, K = map(int, input().split())

sieve = [True] * (N + 1)
cnt = 0

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        print(i, j)
        if sieve[j]:
            sieve[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break
