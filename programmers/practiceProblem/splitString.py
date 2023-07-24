def solution(s):
    answer = 0

    while True:
        count += 1
        x = s[0]
        x_count = 1
        xx_count = 0

        for i in range(len(s)):
            if x == s[i]:
                x_count += 1
            else:
                xx_count += 1

            if x_count == xx_count:
                break
        
        s = s[:x_count]
    
    return answer

s = input()
result = solution(s)
print(result)