# 2월 14일 상

def solution(babbling):
    answer = 0
    # 가능한 발음
    words = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # 비교 단어
        comp = ""
        # 현재 단어
        temp = ""
        
        for w in word:
            temp += w
            
            # 연속 발음 불가
            if temp == comp:
                break
            
            # 발음되는 경우 -> 현재 temp를 comp에 저장 (이후 연속 발음인지 확인하기 위해)
            if temp in words:
                comp = temp
                temp = ""
        
        # 더 이상 확인할 글자가 없는 경우 모두 발음이 되는 것 -> answer += 1
        if temp == "":
            answer += 1
    
    return answer
    
    

# def solution(babbling):
#     answer = 0
#     words = ["aya", "ye", "woo", "ma"]
    
#     # set으로 변경함으로 중복값 제거
#     babbling = set(babbling)
#     babbling = list(babbling)
    
#     # print("init", babbling)
#     init = []
    
#     # 연속 같은 발음 제거
#     for babble in babbling:
#         if "aya" * 2 not in babble and "ye" * 2 not in babble and "woo" * 2 not in babble and "ma" * 2 not in babble:
#             init.append(babble)
            
#     # print("remove", init)
    
#     for i in range(len(init)):
#         temp = ""
#         for j in init[i]:
#             temp += j
#             print("temp1", temp)
#             if temp in words:
#                 print("temp2!!!!!", temp)
#                 print("string@@", init[i][len(temp):])
#                 init[i] = init[i][len(temp):]
#                 temp = ""
#                 print(j, init[i])
    
#     print("last", init)
    
#     for word in init:
#         if word == "":
#             answer += 1

    
#     return answer