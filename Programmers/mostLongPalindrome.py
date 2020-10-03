# 1차 시도. 71.5점. 효율성 테스트 한 개는 실패, 한 개는 성공.
def solution(s):
    answer = 1

    for i in range(1, len(s) - 1):
        for j in range(1, i + 1):
            if s[i - j:i] == s[i + j:i:-1]:
                answer = max(answer, 2 * j + 1)
    return answer

# 2차 시도. 69.3점. 효율성 테스트에서 모두 시간 초과가 난다.
def solution(s):
    answer = 1

    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            if s[i:j] and str(s[i:j]) == str(s[i:j])[::-1]:
                answer = max(answer, len(s[i:j]))
            if s[j:i] and str(s[j:i]) == str(s[j:i])[::-1]:
                answer = max(answer, len(s[j:i]))
    return answer

# 3차 시도. 성공. 1차 시도와 비슷한 O(n^2) 코드이다.
# 하지만 단순히 부분 문자열 길이를 늘려가며 비교해주었다.
def isPalindrome(s):
    return s == s[::-1]

def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if isPalindrome(s[i:j]):
                answer = max(answer, len(s[i:j]))
    return answer