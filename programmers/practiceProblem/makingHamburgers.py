def solution(ingredient):
    answer = 0
    hamburgers = '1231'

    finding = ''.join(str(s) for s in ingredient) # 숫자 원소들을 문자로 만들고 join
    print(finding) # 확인용
    
    while True:
        if hamburgers in finding:
            finding = finding.replace('1231', "").strip() # 찾아서 '1231'를 공백으로 바꾸고 strip()을 이용해서 불필요한 문자 삭제
            answer += 1
            continue
        else:
            break

    return answer
    

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
result = solution(ingredient)
print(result)   