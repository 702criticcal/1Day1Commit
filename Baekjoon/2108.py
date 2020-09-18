# 사실 며칠 전에 풀었던 문제인데 총 7번의 시간초과로 잠깐 포기했었던 문제다...
# Python3 대신 PyPy3로 제출했더니 마지막으로 제출했던 똑같은 코드로 성공했다....
from collections import Counter

N = int(input())
num_lst = sorted([int(input()) for _ in range(N)])
most_commons = Counter(num_lst).most_common(2)

print(round(sum(num_lst) / N))
print(num_lst[N // 2])
if N == 1:
    print(most_commons[0][0])
else:
    print(most_commons[1][0] if most_commons[0][1] == most_commons[1][1] else most_commons[0][0])
print(num_lst[-1] - num_lst[0])
