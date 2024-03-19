# 3월 18일 중

def solution(string):
    answer = 0
    
    
    for i in range(len(string)):
        stack = []
        new_strings = string[i:] + string[:i]
        
        for j in range(len(new_strings)):
            
            if not stack:
                stack.append(new_strings[j])
            else:
                if new_strings[j] == '[' or new_strings[j] == '{' or new_strings[j] == '(':
                    stack.append(new_strings[j])
                elif new_strings[j] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        break
                elif new_strings[j] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        break
                elif new_strings[j] == ')':
                    if stack[-1] == '(':
                        stack.pop()
            
            if j == len(new_strings) - 1 and stack == []:
                answer += 1
                
    
    return answer