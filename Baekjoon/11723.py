import sys
# input()을 사용하면 시간초과가 난다.
input = sys.stdin.readline

S = set([])

for _ in range(int(input())):
    operator = input().split()

    if operator[0] == 'check':
        if int(operator[1]) in S:
            print(1)
        else:
            print(0)

    elif operator[0] == 'toggle':
        if int(operator[1]) in S:
            S.remove(int(operator[1]))
        else:
            S.add(int(operator[1]))

    elif operator[0] == 'add':
        # 조건문없이 실행하면 런타임 에러가 뜬다.
        if int(operator[1]) in S:
            continue
        else:
            S.add(int(operator[1]))

    elif operator[0] == 'remove':
        # 조건문없이 실행하면 런타임 에러가 뜬다.
        if int(operator[1]) not in S:
            continue
        else:
            S.remove(int(operator[1]))

    elif operator[0] == 'all':
        S = set([i for i in range(1, 21)])

    elif operator[0] == 'empty':
        S.clear()
