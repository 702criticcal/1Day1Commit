def solution(s, n):
    caesarPwd = ''
    for i in s:
        if i == ' ':
            caesarPwd += ' '
        else:
            if 65 <= ord(i) <= 90:
                if ord(i) + n <= 90:
                    caesarPwd += chr(ord(i) + n)
                else:
                    caesarPwd += chr(ord(i) - 26 + n)
            elif 97 <= ord(i) <= 122:
                if ord(i) + n <= 122:
                    caesarPwd += chr(ord(i) + n)
                else:
                    caesarPwd += chr(ord(i) - 26 + n)
    return caesarPwd