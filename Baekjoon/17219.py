import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sites = {}

for _ in range(N):
    site, pwd = input().split()
    sites[site] = pwd

for _ in range(M):
    search_site = input().strip()
    print(sites[search_site])
