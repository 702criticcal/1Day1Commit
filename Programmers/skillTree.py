def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        skill_lst = []
        isOK = True
        for j in i:
            if j in skill:
                skill_lst.append(j)

        for k in range(len(skill_lst)):
            if skill_lst[k] != skill[k]:
                isOK = False
                break

        if isOK:
            answer += 1

    return answer