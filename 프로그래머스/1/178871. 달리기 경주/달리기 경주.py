# 3월 4일 상

def solution(players, callings):
    play = {}
    
    for i in range(len(players)):
        play[players[i]] = i

    
    for calling in callings:
        
        idx = play[calling]

        play[calling] = idx - 1
        players[idx] = players[idx -1]

        play[players[idx - 1]] = idx
        players[idx - 1] = calling

    
    return players