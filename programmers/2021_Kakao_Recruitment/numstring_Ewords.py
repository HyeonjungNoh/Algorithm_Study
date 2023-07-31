def solution(s):
    answer = "" # 숫자만
    temp_word = ""  # 영단어(영문자) 임시 저장소
    word_to_number = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for c in s:
        if  c.isdigit():
            answer += c
        else:
            temp_word += c
            if temp_word in word_to_number:
                answer += word_to_number[temp_word]
                temp_word = ""

    answer = int(answer)
    return answer


s = "one4seveneight"
result = solution(s)
print(result)