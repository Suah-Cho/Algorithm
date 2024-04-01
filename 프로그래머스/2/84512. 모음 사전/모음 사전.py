# 3월 26일 상

def solution(word):
    answer = 0
    
    words = ['A', 'E', 'I', 'O', 'U']
    stack = []
    
    for i in range(len(word)):
        print(word[i])
        
        print(stack)
        if not stack or word[i] == stack[-1]:
            stack.append(word[i])
            continue
        else:
            idx = words.index(word[i])
            print(idx, idx * 5 + len(stack), len(stack))
            stack = []
        
        
        stack.append(word[i])
    
    
    return answer