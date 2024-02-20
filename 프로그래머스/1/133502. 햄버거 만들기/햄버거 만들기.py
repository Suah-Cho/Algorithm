# 2월 20일 상

def solution(ingredient):
    answer = 0
    
    temp = []
    for i in ingredient:
        temp.append(i)
        
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            # temp에서 해당하는 값 제거
            del temp[-4:] # del 함수를 사용하여 [-4:]에 해당하는 값 제거
        
    
    return answer

# 시간 초과 1
# def solution(ingredient):
#     answer = 0
#     ing = ''.join(list(map(str, ingredient)))

#         temp = ""
#         for i in ing:
#             temp += i
#             if '1231' in temp:
#                 answer += 1
#                 temp = temp.replace('1231', '')
#     return answer

# 시간 초과 2
# def solution(ingredient):
#     answer = 0
    
#     temp = []
#     for i in ingredient:
#         temp.append(i)
        
#         if temp[-4:] == [1, 2, 3, 1]:
#             answer += 1
#             # temp에서 해당하는 값 제거
#             temp = temp[:-4]
        
    
#     return answer