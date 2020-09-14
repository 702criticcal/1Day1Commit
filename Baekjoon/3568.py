s = list(input().strip(';').split(', '))
s = s[0].split() + s[1:]
type = s.pop(0)
command = []
for i in range(len(s)):
    command.append([type, s[i]])

for i in range(len(command)):
    if not command[i][1].isalpha():
        while True:
            if not command[i][1][-1].isalpha():
                if command[i][1][-1] == ']':
                    command[i][0] += '[]'
                    command[i][1] = command[i][1][:-2]
                else:
                    command[i][0] += command[i][1][-1]
                    command[i][1] = command[i][1][:-1]
            else:
                break

for i in range(len(command)):
    print(' '.join(command[i]) + ';')
