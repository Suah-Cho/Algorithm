# 2월 20일 상

def solution(ingredient):
    answer = 0
    
    temp = []
    for i in range(len(ingredient)):
        temp.append(i)
        
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            # temp 초기화
            temp = temp[:-5]
            print("temp", temp)
        
    
    return answer

# 시간 초과
# ing = ''.join(list(map(str, ingredient)))
    
#     temp = ""
#     for i in ing:
#         temp += i
#         if '1231' in temp:
#             answer += 1
#             temp = temp.replace('1231', '')