import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    checkList = list(map(str, sys.stdin.readline().split()))
    first = checkList[0]
    second = checkList[1]
    firstStr = ''.join(first)
    secondStr = ''.join(second)
    if sorted(first) == sorted(second):
        print(f'{firstStr} & {secondStr} are anagrams.')
    else:
        print(f'{firstStr} & {secondStr} are NOT anagrams.')
