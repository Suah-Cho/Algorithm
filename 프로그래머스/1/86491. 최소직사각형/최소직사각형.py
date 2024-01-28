def solution(sizes):
    x_arr = []
    y_arr = []    
    
    for size in sizes:
        if size[0] > size[1]:
            x_arr.append(size[0])
            y_arr.append(size[1])
        else:
            x_arr.append(size[1])
            y_arr.append(size[0])
    
    return max(x_arr) * max(y_arr)