def solution(k, m, score):
    answer = 0
    tmp = []
    score_sort = sorted(score ,reverse=True) # 내림차순으로 정렬
    throwaway = len(score_sort) % m # 남은 사과 버리기
    
    if throwaway == 0:
        pass
    else:
        score_sort = score_sort[:-throwaway]
        
    for score in score_sort:
        tmp.append(score)
        if len(tmp) == m:
            value = min(tmp)
            crate_price = value * m 
            answer += crate_price
            tmp = []

    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
result = solution(k, m, score)
print(result)