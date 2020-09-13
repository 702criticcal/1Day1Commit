S = input()
answer = ''

for c in S:
    if 65 <= ord(c) <= 77 or 97 <= ord(c) <= 109:
        answer += chr(ord(c) + 13)
    elif 78 <= ord(c) <= 90 or 110 <= ord(c) <= 122:
        answer += chr(ord(c) - 13)
    else:
        answer += c

print(answer)
