for case in range(1, int(input()) + 1):
    stack = []
    List = list(input().split())
    for i in range(len(List)):
        stack.append(List.pop())
    result = ' '.join(stack)
    print(f'Case #{case}: {result}')
