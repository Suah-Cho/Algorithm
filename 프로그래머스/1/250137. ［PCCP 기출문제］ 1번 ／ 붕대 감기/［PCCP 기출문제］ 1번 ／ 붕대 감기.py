# 3월 6일 상

def solution(bandage, health, attacks):
    
    t, x, y = bandage
    
    # 마지막 공격 시간
    last = attacks[-1][0]
    
    # 현재 체력, 연속 공격
    current_health, healing, cont = health, 0, 0
    
    for i in range(1, last + 1):
        healing += 1
        cont += 1
        
        for attack in attacks:
            if attack[0] == i:
                current_health -= attack[1]
                healing, cont = 0, 0
                
        # 캐릭터 사망
        if current_health <= 0:
            return -1
        
        if healing != 0 and cont != 0:
            current_health += x

        if cont == t:
            current_health += y
                 
        if healing == t:
            healing, cont = 0, 0
            
        if current_health > health:
            current_health = health
        
    
    return current_health

# def solution(bandage, health, attacks):
    
#     # 만땅 체력
#     full = health
    
#     # 이전 공격(시간)
#     pre_attack = 0
    
#     while attacks:

#         attack = attacks.pop(0)
#         # print(attack)
        
#         if attack[0] - pre_attack - 1 >= bandage[0]:
#             if health + (attack[0] - pre_attack - 1) * bandage[1] + bandage[2] >= full:
#                 health = full
#             else:
#                 health += (attack[0] - pre_attack - 1) * bandage[1] + bandage[2]
#         else:
#             if health + (attack[0] - pre_attack - 1) * bandage[1] + bandage[2] >= full:
#                 health = full
#             else:
#                 health += (attack[0] - pre_attack - 1) * bandage[1]
#         # print("health", health)
        
#         health = health - attack[1]
#         # print("after attack health", health)
        
#         # 캐릭터가 죽는지 확인
#         if health <= 0:
#             # print("캐릭터가 사망했습니다.")
#             return -1
        
#         pre_attack = attack[0]
    
#     return health