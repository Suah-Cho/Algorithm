# 2월 21일 상

def solution(wallpaper):
    
    isfullx = []
    isfully = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            # print(i, j)
            if wallpaper[i][j] == '#':
                # isfull.append([i, j])
                isfullx.append(i)
                isfully.append(j)
    
    
    return [min(isfullx), min(isfully), max(isfullx) + 1, max(isfully) + 1]