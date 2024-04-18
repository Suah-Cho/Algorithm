from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    d = deque(people)
    
    while len(d) > 1:
        
        # 가장 무거운 사람 + 가장 가벼운 사람 <= limit 인 경우
        if d[0] + d[-1] <= limit:
            # 가장 가벼운 사람 pop
            d.popleft()
        
        # 조건에 해당하지 않는 경우 = 1명만 타야하는 경우
        answer += 1
        # 무거운 사람
        d.pop()
    
    # 홀수로 큐에 아직 남아있는 경우 
    # -> while 조건을 >= 1로 하지 않는 이유는 그렇게 되면 d[0] == d[-1]로 popleft()와 pop()을 하게 되면 런타임에러가 날 수도 있다.
    if d:
        answer += 1
        
        
    return answer

# def solution(people, limit):
#     answer = []
    
#     people.sort()
    
#     while people:
        
#         boat = []
        
#         p = people.pop()
#         # print(p)
        
#         if limit - p < 40 or not people:
#             answer.append([p])
#         else:
#             for i in range(len(people)):
#                 if p + people[i] <= limit:
#                     answer.append([p, people[i]])
#                     people.pop(i)
#                     break
                    
#         # print(people, answer)
    
#     return len(answer)
    
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
    
    