N = int(input())
A, B = map(int, input().split())
C = int(input())
D = sorted([int(input()) for _ in range(N)])
res = C // A
greedy = [C]

while N > 0:
    greedy.append(D.pop())
    temp = sum(greedy) // (A + B * (len(greedy) - 1))
    if res < temp:
        res = temp
    N -= 1
print(res)
