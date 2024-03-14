# 3월 14일 상

# 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.
# n = 5
import math

def solution(citations):
    answer = 0
    
    citations = sorted(citations)
    
    for i in range(len(citations)):
        
        if citations[i] >= len(citations) - i:
            answer += 1
    
#     while not loop:
#         print("now i", i)
        
#         if len(citations[i:]) >= citations[i] and max(citations[:i]) < citations[i]:
#             # h-index = citations[i]
#             loop = True
            
#         else:
#             i -= 1        
    
    return answer