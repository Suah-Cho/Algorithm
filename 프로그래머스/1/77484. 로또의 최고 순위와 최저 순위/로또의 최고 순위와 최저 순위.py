# 2월 28일 상

def solution(lottos, win_nums):
    answer = []
    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    cnt = 0
    zero = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            win_nums.remove(lotto)
            cnt += 1
        if lotto == 0:
            zero += 1
    
    result = [cnt + zero, cnt]
    
    for r in result:
        answer.append(score[r])

    
    return answer