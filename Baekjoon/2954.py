diary = input()
result = ''
idx = 0

while idx < len(diary):
    result += diary[idx]
    if diary[idx] in ['a', 'e', 'i', 'o', 'u']:
        idx += 2
    idx += 1
print(result)
