N = int(input())
seats = list(input().replace('LL', 'L'))
if 'L' in seats:
    print(len(seats) + 1)
else:
    print(len(seats))
