def solution(lottos, win_nums):
    answer = []
    zero_count = 0 # 경우의 수
    find_answer_num = 0 #  최소 정답 개수
    minnum = 0
    maxnum  = 0

    result_dict = {
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 0
    }

    for num in lottos:
        if num == 0:
            zero_count += 1

        elif num in win_nums:
            find_answer_num += 1

        else:
            pass
    
    # 당첨 번호 찾기
    minnum = find_answer_num
    maxnum = find_answer_num + zero_count

    if minnum == 1 or minnum == 0:
        minnum = 0

    
    # 당첨 등수 찾기
    for key, val in result_dict.items():
        if maxnum == val:
            answer.append(key)

    for key, val in result_dict.items():
        if minnum == val:
            answer.append(key)
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
result = solution(lottos, win_nums)
print(result)