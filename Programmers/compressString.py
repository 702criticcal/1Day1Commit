def solution(s):
    if len(s) == 1:
        return 1

    answer = len(s)

    # 압축할 수 있는 문자열의 최대 길이는 길이 / 2까지이다.
    for cut in range(1, len(s) // 2 + 1):
        result = ''
        cnt = 1
        temp_str = s[:cut]
        # 1부터 길이 / 2까지 잘라서 문자열 비교.
        for i in range(cut, len(s) + cut, cut):
            # 앞의 자른 문자열과 같다면 cnt + 1.
            if s[i:i + cut] == temp_str:
                cnt += 1
            # 다르다면, cnt가 1이면 문자열만 결과에 추가하고, cnt가 1이 아니면 숫자와 문자열을 결과에 추가한다.
            else:
                if cnt == 1:
                    result += temp_str
                else:
                    result += str(cnt) + temp_str
                # 자를 문자열 크기 만큼 인덱스를 옮겨서 다시 비교 수행.
                temp_str = s[i:i + cut]
                # 카운트 초기화
                cnt = 1
        # 해당 길이만큼 다 잘랐다면 전체 결과 값과 해당 길이의 결과 값의 최솟값을 구하여 전체 결과값에 저장.
        answer = min(answer, len(result))
    return answer