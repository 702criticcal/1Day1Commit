N = list(map(int, input()))
num_set = [0] * 10

for i in N:
    if i == 6 or i == 9:
        num_set[6] += 1
    else:
        num_set[i] += 1

if num_set[6] % 2 == 0:
    num_set[6] = num_set[6] // 2
else:
    num_set[6] = num_set[6] // 2 + 1

print(max(num_set))
