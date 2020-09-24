# 장르마다 전체 재생횟수를 계산하는 딕셔너리와
# 장르별로 노래를 인덱스값을 넣어 저장한 딕셔너리 두개가 필요하다는 것을 인식하면 이해하기 쉬운 문제.
# 하지만 딕셔너리 두 개가 필요하다는 것을 경험이 없어 처음에 인식하기 힘들었다..
from collections import defaultdict


def solution(genres, plays):
    answer = []
    genres_plays = defaultdict(int)
    genres_songs = defaultdict(lambda: [])
    i = 0

    for g, p in zip(genres, plays):
        genres_plays[g] += p
        genres_songs[g].append((i, p))
        i += 1

    sorted_genres = sorted(genres_plays.items(), key=(lambda x: x[1]), reverse=True)

    for g in sorted_genres:
        sorted_g = sorted(genres_songs[g[0]], key=(lambda x: x[1]), reverse=True)
        answer.append(sorted_g[0][0])
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])

    return answer
