N = int(input())
count = 0
for i in range(N):
    alpabetList = []
    s = input()
    alpabetList.append(s[0])
    if len(s) == 1:
        count += 1
    else:
        for j in range(1, len(s)):
            if s[j - 1] != s[j]:
                if s[j] in alpabetList:
                    break
                else:
                    alpabetList.append(s[j])
            if j == len(s) - 1:
                count += 1
print(count)
