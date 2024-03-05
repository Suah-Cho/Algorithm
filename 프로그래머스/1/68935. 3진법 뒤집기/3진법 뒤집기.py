# 3월 5일 하

def solution(n):
    answer = 0
    three = []
    
    while n > 0:
        n, r = divmod(n, 3)
        three.append(str(r))
    
    # three에 애초에 순서가 뒤바뀌어서 입력된다. 다시 바꿀 필요 no
    thr = ''.join(three)
    
    answer = int(thr, 3)
    
    return answer