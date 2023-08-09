def solution(n, k, enemy):
    answer = 0

    for e in enemy:
        need_Soldiers = e # 필요한 병사
     
        if k > 0:
            need_Soldiers = max(need_Soldiers-n, 0)
            k -= 1
        
        if need_Soldiers > n:
            break
        else:
            n -= need_Soldiers
            answer += 1

    return answer

n = 2 # 병사 수
k = 4 # 무적권
enemy = [3, 3, 3, 3]# 매 라운드마다 공격해오는 적의 수
result = solution(n, k, enemy)
print(result)