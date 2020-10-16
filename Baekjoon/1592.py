N, M, L = map(int, input().split())
friends = [0] * N
friends[0] = 1
ball = 0

while M not in friends:
    if friends[ball] % 2 != 0:
        if ball + L >= N:
            ball = ball + L - N
        else:
            ball = ball + L
        friends[ball] += 1
    else:
        if ball - L < 0:
            ball = N + ball - L
        else:
            ball = ball - L
        friends[ball] += 1

print(sum(friends) - 1)
