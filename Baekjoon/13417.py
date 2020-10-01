from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    cards = list(reversed(list(input().split())))
    deq = deque([cards.pop()])

    while cards:
        c = cards.pop()

        if ord(deq[0]) >= ord(c):
            deq.appendleft(c)
        else:
            deq.append(c)
    print(''.join(deq))
