# Counter 사용.
import sys
from collections import Counter

N = int(sys.stdin.readline())
card_lst = Counter(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))

for num in num_lst:
    if num in card_lst:
        print(card_lst[num], end=' ')
    else:
        print(0, end=' ')

# Counter 미사용.
import sys

N = int(sys.stdin.readline())
card_lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
hash = {}

for card in card_lst:
    if card in hash:
        hash[card] += 1
    else:
        hash[card] = 1

for num in num_lst:
    if num in hash:
        print(hash[num], end=' ')
    else:
        print(0, end=' ')
