# 2월 16일 상

def solution(participant, completion):
    answer = ''
    part_dict = {}
    num = 0
    
    for part in participant:
        part_dict[hash(part)] = part
        num += hash(part)
    
    print(part_dict)
    print(num)
    
    for com in completion:
        num -= hash(com)
        
    print(num)
           
    
    
    return answer

#     효율성 0 점
#     participants = {part : participant.count(part) for part in participant}
#     completions = {com : completion.count(com) for com in completion}
    
#     for key, value in participants.items():
#         if key not in completions:
#             answer += key
#         elif value > completions[key]:
#             answer += key