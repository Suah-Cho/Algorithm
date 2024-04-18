from collections import deque

def solution(people, limit):
    answer = []
    
    people.sort()
    
    while people:
        
        boat = []
        
        p = people.pop()
        # print(p)
        
        if limit - p < 40 or not people:
            answer.append([p])
        else:
            for i in range(len(people)):
                if p + people[i] <= limit:
                    answer.append([p, people[i]])
                    people.pop(i)
                    break
                    
        # print(people, answer)
    
    return len(answer)
    
    
    
    
#     idx = []
    
    
#     for i in range(len(people)):
#         # print(i, people[i])
        
#         if i in idx:
#             continue
#         else:
#             if limit - people[i] > 40 and i != len(people) - 1:
#                 for j in range(i + 1, len(people)):

#                     if people[j] <= limit - people[i] and j not in idx:
#                         idx.append(i)
#                         idx.append(j)
#                         answer.append([people[i], people[j]])
#                         break
#             else:
#                 idx.append(i)
#                 answer.append([people[i]])
            
        
#         # print(answer, idx)
        
            
#         # print(answer, idx)
    
    