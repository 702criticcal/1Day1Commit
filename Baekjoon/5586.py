s = input()
cntJOI, cntIOI = 0, 0

for i in range(len(s) - 2):
    if s[i: i + 3] == 'JOI':
        cntJOI += 1
    elif s[i: i + 3] == 'IOI':
        cntIOI += 1

print(cntJOI)
print(cntIOI)
