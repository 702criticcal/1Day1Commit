alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s = input()
cnt = 0
start = 'A'

for i in s:
    idxStart = alphabet.index(start)
    idxS = alphabet.index(i)

    if abs(idxS - idxStart) > 13:
        cnt += 26 - abs(idxS - idxStart)
    else:
        cnt += abs(idxS - idxStart)
    start = i
print(cnt)
