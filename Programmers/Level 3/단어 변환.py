begin, target = "hit", "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def sol(begin, target, words):
    answer = len(words)
    depth = -1
    if target not in words:
        return 0

    answer = DFS(begin, target, words, depth, answer)
    return answer

def DFS(begin, target, words, depth, answer):
    depth += 1
    nextWord = []

    if begin == target:
        if depth <= answer:
            answer = depth
        return answer

    for word in words:
        cnt = 0
        for idx, char in enumerate(word):
            if begin[idx] != char:
                cnt += 1
        if cnt == 1:
            nextWord.append(word)

    newWords = words
    if begin in newWords:
        newWords.remove(begin)

    for begin in nextWord:
        answer = DFS(begin, target, newWords, depth, answer)

    return answer

print(sol(begin, target, words))