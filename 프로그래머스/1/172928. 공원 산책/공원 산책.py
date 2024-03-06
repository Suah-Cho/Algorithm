# 3월 5일 상

def solution(park, routes):
    
    answer = []
    
    for i in range(len(park)):
        if 'S' in park[i]:
            for j in range(len(park[i])):
                if park[i][j] == 'S':
                    loc = [i, j]
    # print("start", loc)
    
    for route in routes:
        d, s = route.split(' ')
        
        if d == 'N':
            # print("North")
            if loc[0] - int(s) < 0:
                continue
            else:
                for i in range(1, int(s) + 1):
                    if park[loc[0] - i][loc[1]] == 'X':
                        break
                    elif park[loc[0] - i][loc[1]] != 'X' and i == int(s):
                        loc[0] -= int(s)
            
        elif d == 'S':
            # print("South")
            if loc[0] + int(s) >= len(park):
                continue
            else:
                # for i in range(loc[0], loc[0] + int(s) + 1):
                for i in range(1, int(s) + 1):
                    if park[loc[0] + i][loc[1]] == 'X':
                        break
                    elif park[loc[0] + i][loc[1]] != 'X' and i == int(s):
                        loc[0] += int(s)
            
        elif d == 'W':
            # print("West")
            if loc[1] - int(s) < 0:
                continue
            else:
                for i in range(1, int(s) + 1):
                    if park[loc[0]][loc[1] - i] == 'X':
                        break
                    elif park[loc[0]][loc[1] - i] != 'X' and i == int(s):
                        loc[1] -= int(s)
            
        elif d == 'E':
            # print("East")
            if loc[1] + int(s) >= len(park[0]):
                continue
            else:
                # for i in range(loc[1], loc[1] + int(s) + 1):
                for i in range(1, int(s) + 1):
                    if park[loc[0]][loc[1] + i] == 'X':
                        break
                    elif park[loc[0]][loc[1] + i] != 'X' and i == int(s):
                        loc[1] += int(s)
        
        # print("location", loc)
    
    
    return loc
