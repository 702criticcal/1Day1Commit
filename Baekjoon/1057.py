n, kim, lim = map(int, input().split())
players = [[i] for i in range(1, n + 1)]
round = 1

while len(players) > 1:
    l = len(players)
    for i in range(0, l // 2):
        players[i] = players[i] + players[i + 1]
        del players[i + 1]

    for i in players:
        if kim in i and lim in i:
            print(round)
            exit()
    round += 1
