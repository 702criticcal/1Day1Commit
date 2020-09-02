S = input()
result = S[0]

for i in range(1, len(S)):
    if S[i] == '-':
        result += S[i + 1]
print(result)
