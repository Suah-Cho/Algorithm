# 3월 25일 상
from queue import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    
    long = 0
    
    days = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    
    while days:
        day = days.popleft()

        if day > long:
            answer.append(1)
            long = day
        else:
            answer[-1] += 1
    
    
    return answer

    # s = []
#     while True:
#             # 하루 진도율 계산
#             for i in range(len(progresses)):
#                 progresses[i] += speeds[i]


#             if progresses[0] >= 100:
#                 for p in progresses:
#                     if p >= 100:
#                         s.append(p)
#                     else:
#                         if not s:
#                             continue
#                         else:
#                             answer.append(len(s))
#                             del progresses[:len(s)]
#                             del speeds[:len(s)]
#                             s.clear()
#                             break
#             if not progresses:
#                 break