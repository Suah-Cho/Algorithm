# 2월 16일 하

def solution(s):
    answer = ''
    arr = []
    
    strings = s.split(' ')
    
    for string in strings:
        word = ''
        for i in range(len(string)):
            if i % 2 == 0:
                word += upper(string[i])
            else:
                word += lower(string[i])
        arr.append(word)
        
    print(arr)
    print((' ').join(arr))
    
    return (' ').join(arr)

def upper(s):
    return s.upper()

def lower(s):
    return s.lower()