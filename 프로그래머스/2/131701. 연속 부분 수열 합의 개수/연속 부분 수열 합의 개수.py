# 3월 26일 중

def solution(elements):
    answer = 0
    numbers = []
    
    print(elements[:-1])
    
    for i in range(1, len(elements) + 1):
        print("i", i)
        for j in range(len(elements)):
            # print("j", j)
            # if j + i >= len(elements):
            #     print(j, sum(elements[j:j+i]), elements[j:(j + i) % len(elements) - 1])
            # else:
                print(j, sum(elements[j:j+i]), elements[j:j+i], j + i, (j + i) % len(elements))
    
    return answer