# 3월 27일 하

def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if not stack:
            if i == ')':
                return False
            else:
                stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
    
    if not stack:
        return True
    else:
        return False
