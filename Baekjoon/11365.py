while True:
    pwd = input()
    if pwd == 'END':
        break
    print(''.join(list(reversed(pwd))))
