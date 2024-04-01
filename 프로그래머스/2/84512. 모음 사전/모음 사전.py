# 3월 26일 상

def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    
    for i, w in enumerate(word):
        answer += words.index(w) * (5 ** (5- i) - 1) // 4 + 1
    
    return answer