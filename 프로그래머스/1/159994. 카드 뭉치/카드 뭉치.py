def solution(cards1, cards2, goal):

    for word in goal:
        if word == cards1[0]:
            if len(cards1) == 1:
                continue
            else:
                cards1.pop(0)
        elif word == cards2[0]:
            if len(cards2) == 1:
                continue
            else:
                cards2.pop(0)
        else:
            return "No"
    
    return "Yes"