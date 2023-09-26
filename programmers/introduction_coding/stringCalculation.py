
def solution(my_string):
    answer = 0
    try:
        answer = eval(my_string)
        return answer
    except:
        return 0

my_string = "3 + 4"
result = solution(my_string)
print(result)

# eval() : 문자열로 표현된 파이썬 표현식을 실행하고 해당 표현식의 결과를 반환하는 역할을 함.