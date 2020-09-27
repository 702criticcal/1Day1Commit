# 1차 시도. 실패.
import sys

input = sys.stdin.readline

N = int(input())
n_lst = [float(input()) for _ in range(N)]

for i in range(1, N):
    n_lst[i] *= n_lst[i - 1] if n_lst[i - 1] > 1 else 1
print(round(max(n_lst), 4))


# 2차 시도. 성공.
# 이 문제를 통해 python의 round 함수 사용 시 주의점에 대해서 알게 되었다.
# 전까진 단순 반올림 함수인 줄로만 알고 있었는데 아니여서 계속 틀렸다.
# round 함수 : 반올림할 자리의 수가 5일 때, 앞자리의 숫자가 짝수면 내림하고 홀수면 올림한다.
import sys

input = sys.stdin.readline

N = int(input())
n_lst = [float(input()) for _ in range(N)]

for i in range(1, N):
    n_lst[i] = max(n_lst[i - 1] * n_lst[i], n_lst[i])
print("%.3f" % max(n_lst))