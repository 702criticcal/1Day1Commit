i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    day = (V // P) * L
    if V % P >= L:
        day += L
    else:
        day += V % P
    print(f'Case {i}: {day}')
    i += 1
