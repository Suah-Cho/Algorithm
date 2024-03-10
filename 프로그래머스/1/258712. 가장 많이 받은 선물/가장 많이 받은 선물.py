# 3월 7일 상

# n(A가 준 선물) > n(B가 준 선물) -> A가 다음 달 선물 받음
# n(A가 준 선물) == n(B가 준 선물) -> 선물 지수가 더 큰 사람이 선물 받음
#   선물 지수 = n(A가 받은 선물) - n(A가 준 선물)
# gifts의 원소 "A B" => A는 선물 준 친구 / B는 선물 받은 친구

# return 가장 많이 받은 선물의 개수

def solution(friends, gifts):
    
    give_get = {}
    next_gifts = {}
    scores = {}
    
    for f in friends:
        next_gifts[f] = 0
        scores[f] = [0, 0] # [give, get]
        
    for gift in gifts:
        if gift in give_get:
            give_get[gift] += 1
        else:
            give_get[gift] = 1
    
    last = []
    
    for key, val in give_get.items():
        give, get = 0, 0

        if key not in last:
            keys = key.split(' ')
            give = val
            last.append(key)

            if keys[1] + ' ' + keys[0] in give_get:
                get = give_get[keys[1] + ' ' + keys[0]]
                last.append(keys[1] + ' ' + keys[0])
            
            scores[keys[0]][0] += give
            scores[keys[0]][1] += get
            scores[keys[1]][0] += get
            scores[keys[1]][1] += give

                
    # print(scores)
    
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            # print(friends[i], friends[j])
            give, get = 0, 0
            
            if friends[i] + ' ' + friends[j] in give_get or friends[j] + ' ' + friends[i] in give_get:
                if friends[i] + ' ' + friends[j] in give_get:
                    give = give_get[friends[i] + ' ' + friends[j]]
                if friends[j] + ' ' + friends[i] in give_get:
                    get = give_get[friends[j] + ' ' + friends[i]]
            
            if give > get:
                next_gifts[friends[i]] += 1
            elif get > give:
                next_gifts[friends[j]] += 1
            elif give == get:
                if scores[friends[i]][0] - scores[friends[i]][1] > scores[friends[j]][0] - scores[friends[j]][1]:
                    next_gifts[friends[i]] += 1
                elif scores[friends[j]][0] - scores[friends[j]][1] > scores[friends[i]][0] - scores[friends[i]][1]:
                    next_gifts[friends[j]] += 1
            # print(next_gifts)
    
#     print("----------------------------------------------------------------------------------")
#     print(next_gifts)
    
#     print(next_gifts[max(next_gifts,key=next_gifts.get)])
    
    return next_gifts[max(next_gifts,key=next_gifts.get)]