import sys

s = sys.stdin.readline()

for i in range(0, len(s), 10):
    print(s[i:i + 10])
