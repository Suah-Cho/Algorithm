# 2월 27일 상

def solution(board, moves):
    answer = 0
    bucket = []
    
    for i in moves:
        for j in range(5):
            if board[j][i - 1] != 0:
                if not bucket:
                    bucket.append(board[j][i - 1])
                    board[j][i - 1] = 0
                else:
                    if bucket[-1] == board[j][i - 1]:
                        bucket.pop()
                        board[j][i - 1] = 0
                        answer += 2
                    else:
                        bucket.append(board[j][i - 1])
                        board[j][i - 1] = 0
                break
    
    
    return answer