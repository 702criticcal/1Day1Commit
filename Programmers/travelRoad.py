def dfs(countries):
    stack = ["ICN"]
    visited = []

    while stack:
        country = stack[-1] # 현재 있는 공항.
        # 현재 공항에서 출발하는 항공권이 없을 때,
        if country not in countries or len(countries[country]) == 0:
            # 스택에서 pop하여 visited에 해당 공항 추가.
            visited.append(stack.pop())
        # 현재 공항에서 출발하는 항공권이 있을 때, (남아 있을 때)
        else:
            # 스택에 해당 공항에서 갈 수 있는 공항 중 알파벳 순서가 가장 빠른 공항을 스택에 넣는다.
            stack.append(countries[country][-1])
            countries[country] = countries[country][:-1]
    # 최종 도착지 -> 출발지 순서로 삽입되었기 때문에 역순으로 출력해준다.
    return list(reversed(visited))


def solution(tickets):
    # 2차원 리스트로 저장된 tickets를 출발지:도착지 형태의 딕셔너리로 저장한다.
    countries = {}
    for c in tickets:
        try:
            countries[c[0]] += [c[1]]
        except:
            countries[c[0]] = [c[1]]

    # 모든 출발할 수 있는 공항의 도착지를 알파벳 역순으로 정렬해준다.
    # dfs 메소드 실행 시, 가장 뒤에 있는 요소가 알파벳 순서가 가장 빠른 공항이 되게 하기 위해서이다.
    for k in countries:
        countries[k] = sorted(countries[k], reverse=True)

    return dfs(countries)