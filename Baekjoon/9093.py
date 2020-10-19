for _ in range(int(input())):
    sentence = input().split()
    for i, s in enumerate(sentence):
        sentence[i] = s[::-1]
    print(' '.join(sentence))
