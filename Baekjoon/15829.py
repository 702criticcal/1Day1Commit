# 1차 시도. 64ms 성공. 딕셔너리 처리한게 너무 별로인 것 같아 수정하고 싶다. 딕셔너리가 아니라도 문자열 인덱스도 사용 가능 할 듯 싶다 !
sToNumDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
              't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

L = int(input())
string = input()
numbering = []
sum = 0

for s in string:
    numbering.append(str(sToNumDict[s]))

for i, v in enumerate(numbering):
    sum += int(v) * (31 ** i)
print(sum % 1234567891)

# 2차 시도. 64ms 성공. 딕셔너리로 매핑 대신 아스키 코드 값 - 96 사용하여 시간은 똑같지만 코드 길이를 333 B 줄였다 !
L = int(input())
string = input()
sum = 0

for i in range(len(string)):
    sum += (ord(string[i]) - 96) * (31 ** i)
print(sum % 1234567891)
