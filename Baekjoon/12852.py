from collections import deque

N = int(input())
queue = deque([N])
num_lst = [[0, []] for _ in range(N + 1)]

while queue:
    x = queue.popleft()
    if x == 1:
        print(num_lst[1][0])
        print(' '.join(list(map(str, num_lst[1][1] + [1]))))
        exit()

    if x % 3 == 0 and num_lst[x // 3][0] == 0:
        queue.append(x // 3)
        num_lst[x // 3][0] = num_lst[x][0] + 1
        num_lst[x // 3][1] = num_lst[x][1] + [x]

    if x % 2 == 0 and num_lst[x // 2][0] == 0:
        queue.append(x // 2)
        num_lst[x // 2][0] = num_lst[x][0] + 1
        num_lst[x // 2][1] = num_lst[x][1] + [x]

    if num_lst[x - 1][0] == 0:
        queue.append(x - 1)
        num_lst[x - 1][0] = num_lst[x][0] + 1
        num_lst[x - 1][1] = num_lst[x][1] + [x]
