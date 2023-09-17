def solution(wallpaper):
    answer = []
    in_file_x = []
    in_file_y = []
    
    lux = luy = rdx = rdy = -1
    
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[0])) :
            if wallpaper[i][j] == '#' :
                in_file_x.append(i)
                in_file_y.append(j)

    startedge = [min(in_file_x), min(in_file_y)]
    endedge = findendedge(max(in_file_x), max(in_file_y))

    answer.append(startedge[0])
    answer.append(startedge[1])
    answer.append(endedge[0])
    answer.append(endedge[1])
                    
    return answer

def findendedge(x, y) :
    edge = []
    edge.append(x+1)
    edge.append(y+1)
    
    return edge