N = int(input())
num_lst = list(map(int, input().split()))
biggest = max(num_lst)
cnt = 0
sieve = [False, False] + [True] * (biggest - 1)

for i in range(biggest + 1):
    if sieve[i] == True:
        for j in range(2 * i, biggest + 1, i):
            sieve[j] = False

for i in num_lst:
    if sieve[i] == True:
        cnt += 1
print(cnt)
