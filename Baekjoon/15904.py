def check_ucpc(s):
    if 'U' not in s or 'C' not in s or 'P' not in s:
        return 'I hate UCPC'

    for i in range(s.index('U'), len(s)):
        if s[i] == 'C':
            for j in range(i + 1, len(s)):
                if s[j] == 'P':
                    for k in range(j + 1, len(s)):
                        if s[k] == 'C':
                            return 'I love UCPC'

    return 'I hate UCPC'


print(check_ucpc(input()))
