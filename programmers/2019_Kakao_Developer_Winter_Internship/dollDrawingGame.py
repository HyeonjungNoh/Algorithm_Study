def solution(board, moves):
    answer = 0
    basket = []
   

    for doll in moves:
        col = doll - 1

        for row in range(len(board)): # pop할 인형 찾기
            if board[row][col] != 0:
                pick_doll = board[row][col]
                board[row][col] = 0 # 인형 잡음 -> 0으로 칸 비움

                if basket and basket[-1] == pick_doll: # 빈 바구니 x 잡아 올린 인형이 pick_doll 이랑 같은지 검사
                    basket.pop()
                    answer += 2
                else:
                    basket.append(pick_doll)
                break

    return answer


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

result = solution(board, moves)
print(result)


