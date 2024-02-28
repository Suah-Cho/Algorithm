# 2월 27일 상

def solution(board, moves):
    answer = 0
    basket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                if not basket:
                    basket.append(board[j][i - 1])
                    board[j][i - 1] = 0
                else:
                    if basket[-1] == board[j][i - 1]:
                        basket.pop()
                        board[j][i - 1] = 0
                        answer += 2
                    else:
                        basket.append(board[j][i - 1])
                        board[j][i - 1] = 0
                break
    
    
    return answer