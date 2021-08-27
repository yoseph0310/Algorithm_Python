def solution(skill, skill_trees):
    skill = list(skill)
    flag = []

    for i in skill_trees:
        post_skill_trees = []
        for j in list(i):
            if j in skill:
                post_skill_trees.append(j)

        for idx, j in enumerate(post_skill_trees):
            if j != skill[idx]:
                flag.append(-1)
                break

    return len(skill_trees) + sum(flag)