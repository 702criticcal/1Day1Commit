import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pokemons = {}
for i in range(1, N + 1):
    p = input().strip()
    pokemons[i] = p
    pokemons[p] = i

for i in range(M):
    q = input().strip()
    if q.isdigit():
        print(pokemons[int(q)])
    else:
        print(pokemons[q])
