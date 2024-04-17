def solution(brown, yellow):
    
    a = brown + yellow
    
    w, h = 3, 1
    
    while True:
        
        h = a // w
        r = a % w
        
        if r == 0 and w >= h and yellow == (w - 2) * (h - 2):
            return [w, h]
        
        w += 1
    
