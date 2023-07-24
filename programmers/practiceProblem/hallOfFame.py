def solution(k, score):
    answer = []
    fame = []

    for i in range(len(score)):
        if i < k:
            fame.append(score[i])
            fame.sort(reverse=True)
            answer.append(fame[-1])

        else:
            fame.append(score[i])
            fame.sort(reverse=True)
            fame = fame[0:k]
            answer.append(fame[-1])

    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
result = solution(k, score)
print(result)


