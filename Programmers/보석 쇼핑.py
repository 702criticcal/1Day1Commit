from collections import defaultdict


def solution(gems):
    gemNum = len(gems)  # 전체 보석 진열대의 길이 저장.
    gemKind = len(set(gems))  # 전체 보석 진열대에 놓인 보석들의 종류 저장.
    answer = [0, gemNum]  # 길이의 최솟값 저장.
    kindDict = defaultdict(int)  # 탐색 길이 내의 보석의 종류마다 개수를 저장하기 위한 딕셔너리.
    kindDict[gems[0]] = 1

    start, end = 0, 0  # 길이의 시작 지점, 끝 지점 지정.
    while start < len(gems) and end < len(gems):
        # 길이 내의 보석 종류가 전체 보석 종류의 개수와 같다면,
        if len(kindDict) == gemKind:
            # 현재 저장된 길이의 최솟값보다 더 짧은 길이라면,
            if end - start < answer[1] - answer[0]:
                # answer에 현재 값 저장.
                answer = [start + 1, end + 1]
            # 더 짧은 길이를 찾기 위해 start를 +1 해줄거니까 딕셔너리에서도 start에 해당하는 보석의 개수를 하나 줄여줌.
            kindDict[gems[start]] -= 1
            # 개수가 0이라면 len()을 통한 종류 개수를 구할 수 있도록 보석의 종류를 아예 없앰.
            if kindDict[gems[start]] == 0:
                del kindDict[gems[start]]
            start += 1
        # 보석의 종류를 다 포함하지 못하고 있으면,
        else:
            end += 1  # end를 +1하여 길이를 늘린다.
            if end == gemNum:
                break
            # end에 있는 보석도 이제 포함되므로 개수를 +1 해준다.
            kindDict[gems[end]] += 1

    return answer
