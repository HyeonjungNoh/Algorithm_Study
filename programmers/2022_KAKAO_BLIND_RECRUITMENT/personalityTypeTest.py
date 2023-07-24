def solution(survey, choices):
    answer = ''
    
    scores_count = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        score = choices[i]
        if score == 1:
            scores_count[survey[i][0]] += 3 # 매우 비동의
        elif score == 2:
            scores_count[survey[i][0]] += 2 # 비동의
        elif score == 3:
            scores_count[survey[i][0]] += 1 # 약간 비동의
        elif score == 4:
            scores_count[survey[i][0]] += 0 # 모르겠음
        elif score == 5:
            scores_count[survey[i][1]] += 1 # 약간 동의
        elif score == 6:
            scores_count[survey[i][1]] += 2 # 동의 
        elif score == 7:
            scores_count[survey[i][1]] += 3 # 매우 동의

    # print(scores_count) # 확인용
    
    # 각 지표에서 유형 결정
    scores_key = list(scores_count.keys()) 
    scores_value = list(scores_count.values())


    for i in range(0, 8, 2):
        if scores_value[i] > scores_value[i+1]:
            answer += scores_key[i]
        elif scores_value[i] == scores_value[i+1]:
            answer += scores_key[i]
        elif scores_value[i] < scores_value[i+1]:
            answer += scores_key[i+1]
        
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = solution(survey, choices)
print(result)