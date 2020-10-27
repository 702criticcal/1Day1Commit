N, r, c = map(int, input().split())
cnt = 0

while N > 0:
    temp = (2 ** N) // 2

    if r < temp and c >= temp:
        cnt += temp ** 2
        c -= temp
    elif r >= temp and c < temp:
        cnt += (temp ** 2) * 2
        r -= temp
    elif r >= temp and c >= temp:
        cnt += (temp ** 2) * 3
        r -= temp
        c -= temp

    N -= 1

print(cnt)
