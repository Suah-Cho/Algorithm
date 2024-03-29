# 3월 26일 중

def solution(elements):
    numbers = []
    n = len(elements)
    elements += elements[:-1]
    
    for i, element in enumerate(elements):
        sum = element
        numbers.append(sum)
        
        for e in elements[i + 1: i + n]:
            sum += e
            numbers.append(sum)

    return len(list(set(numbers)))