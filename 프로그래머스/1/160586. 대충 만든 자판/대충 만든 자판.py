# 3월 1일 중

def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = 0
        for t in target:
            cnt = []
            for key in keymap:
                if key.find(t) >= 0:
                    cnt.append(key.find(t) + 1)
            

            if not len(cnt):
                count = 0
                break
                
            if len(cnt) >= 1:
                count += min(cnt)

        if count == 0:
            answer.append(-1)
        else:
            answer.append(count)

    
    return answer