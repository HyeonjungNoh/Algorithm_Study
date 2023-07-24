def solution(number, limit, power):
    answer = 0
    divisors = [0] * (number+1)
    divisor_count = 0
    
    #ver1
    # for num in range(1, number+1): # number 까지
    #     for i in range(1, num+1): # 약수 구하기
    #         if num % i == 0:
    #             divisor_count += 1
                
    #     divisors.append(divisor_count)
    #     divisor_count = 0


    # # ver2 
    # for num in range(1, number + 1):
    #     for i in range(num, number + 1, num): # 이전에 계산한 약수 기억함. 시간 효율성 상승
    #         divisors[i] += 1  # num의 배수들에 대해 약수 개수 증가
    

    
    # 공격력 검사
    for j in range(len(divisors)):
        if divisors[j] > limit:
            divisors[j] = power # power 조정
        else:
            pass
            
    print(divisors)
    answer = sum(divisors)
    return answer


number = 10
limit = 3
power = 2
result = solution(number, limit, power)
print(result)

