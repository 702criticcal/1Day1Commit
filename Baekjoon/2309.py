from itertools import combinations

height = [int(input()) for _ in range(9)]
for i in list(combinations(height, 7)):
    if sum(i) == 100:
        result = sorted(i)

for i in result:
    print(i, end= ' ')
