# 2월 15일 상

def solution(N, stages):
    answer = []
    fail_stages = []
    
    num = 0
    for i in range(1, N + 1):
        if len(stages) == num:
            fail_stages.append([0, i])
        else:
            fail_rate = stages.count(i) / (len(stages) - num)
            num += stages.count(i)
            fail_stages.append([fail_rate, i])
        
        
    fail_stages.sort(key=lambda x : (-x[0], x[1]))
    
    for stage in fail_stages:
        answer.append(stage[1])
    
    return answer