# 2월 21일 하

def solution(n, arr1, arr2):
    answer = []
    arr =[]
    
    for num1, num2 in zip(arr1, arr2):
        arr.append([format(num1, 'b').zfill(n), format(num2, 'b').zfill(n)])
            
    for line in arr:
        temp = ""
        for i, j in zip(line[0], line[1]):
            if int(i) or int(j):
                temp += "#"
            else:
                temp += " "
        
        answer.append(temp)
    
    return answer