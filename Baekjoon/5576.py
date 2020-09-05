import sys

wUniversity = []
kUniversity = []

for i in range(20):
    if i < 10:
        wUniversity.append(int(sys.stdin.readline()))
    else:
        kUniversity.append(int(sys.stdin.readline()))

wUniversity.sort(reverse=True)
kUniversity.sort(reverse=True)
print(sum(wUniversity[:3]), sum(kUniversity[:3]))
