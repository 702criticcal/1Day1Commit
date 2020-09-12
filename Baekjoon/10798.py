s_lst = [input() for i in range(5)]

for j in range(15):
    for i in s_lst:
        try:
            if i[j]:
                print(i[j], end='')
        except:
            continue
