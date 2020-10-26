for _ in range(int(input())):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    S = input()
    res = 0

    for s in S:
        if s in alphabet:
            alphabet.remove(s)

    for a in alphabet:
        res += ord(a)

    print(res)
