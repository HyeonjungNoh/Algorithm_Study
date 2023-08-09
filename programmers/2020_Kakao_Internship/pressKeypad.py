def get_distance(hand_dis, target_dis):
    return abs(hand_dis[0] - target_dis[0]) + abs(hand_dis[1] - target_dis[1])


def solution(numbers, hand):
    answer = ''
    keypad = { # 좌표
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }

    L_hand = (3,0) # *위치
    R_hand = (3,2) # #위치

    for number in numbers:
        if number in [1,4,7]: # 왼쪽
            answer += 'L'
            L_hand = keypad[number]

        elif number in [3,6,9]: # 오른쪽
            answer += 'R'
            R_hand = keypad[number]
        
        else: # 가운데 
            l_dis = get_distance(L_hand, keypad[number])
            r_dis = get_distance(R_hand, keypad[number])

            if l_dis < r_dis or (l_dis == r_dis and hand == 'left'):
                answer += 'L'
                L_hand = keypad[number]
            else:
                answer += 'R'
                R_hand = keypad[number]

    return answer



numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = solution(numbers, hand)
print(result)