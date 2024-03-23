# 3월 15일 상

from collections import Counter

def solution(want, number, discount):
    answer = 0
    wants = {} # {'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1}
    
    for w, n in zip(want, number):
        wants[w] = n
        
    for i in range(len(discount)):
        if wants == Counter(discount[i:i+10]):
            answer += 1
    
    return answer

#     for i in range(nums):
#         w = wants
#         if len(discount[i:i+10]) >= nums:
#             dis = discount[i:i+10]
#             print("first", w)
#             for d in dis:
#                 # print(d)
#                 if d in w and w[d] > 0:
#                     w[d] -= 1
            
#             print("---------------")
#             print(w)
            