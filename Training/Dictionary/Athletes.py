from collections import defaultdict

def solution(participant, completion):
    
    dict = defaultdict(int)
    
    for i in participant :
        dict[i] += 1
    
    for i in completion :
        dict[i] -= 1
        
    for name , val in dict.items() :
        if val > 0 :
            return name
    
    
        