def solution(X, Y):
    answer = ''
    mates = []
    mates_int = []

    for c in X:
        if c in Y:
            mates.append(c)
            Y = Y.replace(c,"", 1) # 1의 의미는 첫 번째 발견된 c만 대체

    if len(mates) == 0: #  짝꿍이 존재하지 않으면 
        answer = "-1"
        # print(-1)

    elif all(e == '0' for e in mates): # 짝꿍이 0으로만 구성되어 있다면
        answer = "0"
        # print(0)
    
    else: #  그 외의 경우 가장 큰 수 만들기
        # for e in mates:
        #     mates_int.append(int(e)) # str -> int

        mates_int = sorted([int(e) for e in mates], reverse=True) # 내림 차순 정렬
        mates = [str(e2) for e2 in mates_int] # int -> str 
        answer = ''.join(mates)
            
    return answer


X = "5525"
Y = "1255"
result = solution(X,Y)
print(result)