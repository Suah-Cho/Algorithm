def solution(arr1, arr2):
    answer = []
    sum = []   
    
    for arr_1, arr_2 in zip(arr1, arr2) :
        for num1, num2 in zip(arr_1, arr_2) :
            sum.append(num1+num2)
        answer.append(sum)
        sum = []
    
    return answer