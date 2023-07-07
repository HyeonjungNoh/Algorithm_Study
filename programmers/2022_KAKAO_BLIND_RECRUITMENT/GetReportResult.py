from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_clean = {}
    report_count = {}
    stop_target = []

    # 유저ID -> 딕셔너리로 변경
    for key in id_list: 
        report_count[key] = 0
    # print(idd_list) # 확인용

    report = list(set(report)) # 중복제거

    for string in report:
        split_result = string.split()
        key = split_result[0]
        value = split_result[1]
        report_count[value] += 1 # 신고 접수 카운팅

        if key in report_clean: # 신고 테이블 정리
            report_clean[key].append(value)
        else:
            report_clean[key] = [value]
    
    print(report_clean) # 확인용
    print(report_count) # 확인용

    # 정지할 타켓값 찾고 해당 키 찾아 카운팅
    for key, value in report_count.items():
        if value >= k:
            stop_target.append(key)

    print(stop_target)

    matching_keys = {} # 딕셔너리 만들기
    for key in id_list: 
        matching_keys[key] = 0

    print(matching_keys)

    for target in stop_target:
        for key, value in report_clean.items():
            if target in value:
                matching_keys[key] += 1
            else:
                continue


    print(matching_keys)
    answer = list(matching_keys.values())

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

result = (solution(id_list, report, k))
print(result)







# 엄청 간단하네.....
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer