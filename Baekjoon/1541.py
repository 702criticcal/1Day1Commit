s_lst = input().split('-')
s_lst[0] = sum(map(int, s_lst[0].split('+')))

for i in range(1, len(s_lst)):
    if '+' in s_lst[i]:
        s_lst[i] = -sum(map(int, s_lst[i].split('+')))
    else:
        s_lst[i] = -int(s_lst[i])

print(sum(s_lst))
