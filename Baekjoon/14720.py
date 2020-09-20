N = int(input())
milks = list(map(int, input().split()))
drink = [0, 1, 2]
drink_cnt = 0
cnt = 0

for i in milks:
    if drink[drink_cnt] == i:
        cnt += 1
        drink_cnt += 1
    if drink_cnt == 3:
        drink_cnt = 0
print(cnt)
