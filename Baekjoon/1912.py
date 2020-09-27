# 풀이 코드. 파이썬을 활용하여 문제를 해결하는 만큼 파이써닉 코드를 작성하는 방법을 익혀야 겠다.
import sys

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))

for i in range(1, n):
    # i-1 요소가 0보다 크면 i 요소에 더하여 최댓값을 구함.
    if n_lst[i - 1] > 0:
        n_lst[i] += n_lst[i - 1]
print(max(n_lst))

# 파이썬다운 코드.
import sys

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))

for i in range(1, n):
    # if else 문을 한줄로 구현.
    n_lst[i] += n_lst[i - 1] if n_lst[i - 1] > 0 else 0
print(max(n_lst))



