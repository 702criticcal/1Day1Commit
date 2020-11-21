for _ in range(int(input())):
    players = []
    p = int(input())

    for _ in range(p):
        c, name = input().split()
        players.append([int(c), name])

    players.sort(key=lambda x: x[0])
    print(players[-1][1])
