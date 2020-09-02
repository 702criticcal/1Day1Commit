alphabet = 'abcdefghijklmnopqrstuvwxyz'
countList = [0] * 26
S = input()

for s in S:
    countList[alphabet.index(s)] += 1
print(' '.join(list(map(str, countList))))
