T = int(input())

for _ in range(T):
    animals_word_list = []
    word_lst = list(input().split())

    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        animal, goes, word = s.split()
        animals_word_list.append(word)

    for w in animals_word_list:
        while w in word_lst:
            word_lst.remove(w)

    print(' '.join(word_lst))
