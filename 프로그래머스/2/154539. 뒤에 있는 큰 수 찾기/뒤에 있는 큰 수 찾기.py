# 3월 27일 상

def solution(numbers):
    answer = []
    
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        print(i, numbers[i])
        
        print(numbers[i:])
        
        while stack and numbers[i] >= stack[-1]:
            stack.pop
        
        if not stack:
            answer.append(-1)
        
        stack.append(numbers[i])
        
    print(answer)
    
    return answer


#     for i in range(len(numbers)):
        
#         if  numbers[i] >= max(numbers[i:]):
#             answer.append(-1)
#         else:
#             for num in numbers[i+1:]:
#                 if numbers[i] >= num:
#                     continue
#                 else:
#                     answer.append(num)
#                     break