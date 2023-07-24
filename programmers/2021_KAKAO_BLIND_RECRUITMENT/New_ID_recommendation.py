import re

def solution(new_id):
    answer = ''

    # step1 
    new_id = new_id.lower()
    # print(new_id)

    # step2 
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    # print(new_id)

    # step3
    pattern = r'(\.)\1+'
    new_id = re.sub(pattern, r'\1', new_id)
    # print(new_id)

    # step4
    pattern2 = r'^\.|\.$'
    new_id = re.sub(pattern2, '', new_id)
    # print(new_id)

    # step5
    if len(new_id) == 0:
        new_id = 'a'

    # step6
    if len(new_id) > 15:
        new_id = new_id[:15]
        pattern3 = r'\.$'
        new_id = re.sub(pattern3, '', new_id)
        # print(new_id)

    # step7
    while len(new_id) <3:
        new_id += new_id[-1]
        # print(new_id)

    answer = new_id
    return answer



new_id = "...!@BaT#*..y.abcdefghijklm"
result = solution(new_id)
print(result)