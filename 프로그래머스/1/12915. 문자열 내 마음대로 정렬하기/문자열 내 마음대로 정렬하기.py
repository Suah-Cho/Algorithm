# 2월 15일 하

def solution(strings, n):
    answer = []
    
    string_list = []
    
    for string in strings:
        string_list.append([string[n], string])
    
    # print(string_list) => 	[['u', 'sun'], ['e', 'bed'], ['a', 'car']]
    
    # 정렬
    string_list.sort()
    
    # print(string_list) => 	[['a', 'car'], ['e', 'bed'], ['u', 'sun']]
    
    for string in string_list:
        # print(string)
        answer.append(string[1])
    
    return answer