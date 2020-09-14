t = int(input())

for _ in range(t):
    n = int(input())
    first_public_key = list(input().split())
    second_public_key = list(input().split())

    index_lst = []
    for i in first_public_key:
        index_lst.append(second_public_key.index(i))

    pwd = list(input().split())

    for i in index_lst:
        print(pwd[i], end=' ')
