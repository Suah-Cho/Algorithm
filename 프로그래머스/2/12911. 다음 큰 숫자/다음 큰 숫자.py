# 3월 25일 하

def solution(n):
    # print(bin(n), bin(n).count('1'))
    k = bin(n).count('1')
    
    answer = n + 1
    
    while answer > n:
        if bin(answer).count('1') == k:
            break
        answer += 1
    
    return answer