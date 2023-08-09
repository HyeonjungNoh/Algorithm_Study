import math

def solution(w,h):
    answer = 1
    gcd_result = math.gcd(w,h)
    area = w * h 
    no_square = (w // gcd_result + h // gcd_result -1) * gcd_result
    answer = area - no_square
    return answer

W = 8
H = 12
result = solution(W,H)
print(result)