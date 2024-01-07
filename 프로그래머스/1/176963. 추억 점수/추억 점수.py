def solution(name, yearning, photo):
    
    answer = []
    memories = dict(zip(name, yearning))
    
    for people in photo:
        yearning_num = 0
        
        for person in people:
            yearning_num += memories[person] if memories.get(person) else 0
            
        answer.append(yearning_num)
            
    
    return answer