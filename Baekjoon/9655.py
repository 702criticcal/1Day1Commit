N = int(input())

# 돌을 1개 혹은 3개밖에 가져갈 수 없고, 2개가 남았을 때, 2개를 가져가지 못하고 1개만 가져가야 하므로
# 짝수일 땐 창영이가 이기고, 홀수일 땐, 상근이가 이긴다.
if N % 2 == 0:
    print('CY')
else:
    print('SK')
