# 3월 25일 상

def solution(progresses, speeds):
    answer = []
    
    s = []
    
    # del progresses[:2]
    # del speeds[:2]
    # print(progresses)
    # del progresses[:1]
    # del speeds[:1]
    # print(progresses)
    
    while True:
        # 하루 진도율 계산
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        
        if progresses[0] >= 100:
            for p in progresses:
                if p >= 100:
                    s.append(p)
                else:
                    if not s:
                        continue
                    else:
                        answer.append(len(s))
                        del progresses[:len(s)]
                        del speeds[:len(s)]
                        s.clear()
                        break
        if not progresses:
            break
        
    
    return answer