s = input()
suffix = []

for i in range(len(s)):
    suffix.append(s[i:])

for i in sorted(suffix):
    print(i)
