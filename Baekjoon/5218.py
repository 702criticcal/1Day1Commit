def calc(x, y):
    alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idxX = alphabet.index(x)
    idxY = alphabet.index(y)
    if idxX <= idxY:
        return idxY - idxX
    else:
        return idxY + 26 - idxX


for _ in range(int(input())):
    a, b = input().split()
    answer = []

    for i in range(len(a)):
        answer.append(str(calc(a[i], b[i])))

    print(f"Distances: {' '.join(answer)}")
