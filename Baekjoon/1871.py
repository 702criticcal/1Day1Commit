a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(input())
for _ in range(N):
    car_num = input().split('-')
    alpha = a.index(car_num[0][0]) * (26 ** 2) + a.index(car_num[0][1]) * 26 + a.index(car_num[0][2])
    digit = int(car_num[1])

    if abs(alpha - digit) <= 100:
        print('nice')
    else:
        print('not nice')
