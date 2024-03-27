# 3월 27일 상

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        
        if stack:
            answer[i] = stack[-1]
        
        stack.append(numbers[i])
    
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