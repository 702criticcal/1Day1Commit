# LRU 알고리즘을 구현하는 문제.
def solution(cacheSize, cities):
    answer = 0
    cache = []
    # 캐시 크기가 0일 때는 모든 경우가 cache miss이므로 데이터 개수 * miss 실행 시간을 해준다.
    if cacheSize == 0:
        return len(cities) * 5
    # 데이터마다 캐시를 확인한다.
    for city in cities:
        # 대소문자를 구분하지 않으므로 소문자로 통일하여 확인한다.
        check = city.lower()
        # 캐시 안에 데이터가 없다면,
        if not check in cache:
            # 현재 캐시 안에 있는 데이터의 수가 전체 캐시사이즈보다 작다면, 바로 캐시에 추가해준다.
            if len(cache) < cacheSize:
                cache.append(check)
            # 현재 캐시가 꽉 차있다면, 가장 앞에 있는 것을 pop하고 가장 뒤에 데이터를 추가해준다.
            # 가장 앞에 있는 것을 빼주는 이유는 아래 코드에 있다.
            else:
                cache.pop(0)
                cache.append(check)
            # 캐시가 꽉차든 안찼든 이 경우엔 cache miss이므로 실행시간에 5를 더해준다.
            answer += 5
        # 캐시 안에 현재 실행할 데이터가 이미 있다면,
        else:
            # 해당 데이터의 인덱스를 찾아 pop해주고, 가장 뒤에 다시 넣는다.
            # 이로써 가장 오랫동안 호출되지 않은 데이터는 가장 앞에 있는 데이터가 되는 것이다.
            cache.pop(cache.index(check))
            cache.append(check)
            # 이 경우엔 cache hit이므로 실행시간에 1을 더해준다.
            answer += 1
    return answer