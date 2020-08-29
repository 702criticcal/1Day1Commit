import sys

stick = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
result = [stick.pop()]
for i in stick[::-1]:
    if i > result[-1]:
        result.append(i)
print(len(result))
