# 2월 29일 중

def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    box = []
    for apple in score:
        box.append(apple)
        if len(box) == m:
            answer += min(box) * m
            box.clear()
    
    return answer