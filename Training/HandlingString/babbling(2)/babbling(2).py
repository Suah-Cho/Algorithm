def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for text in babbling :
        for word in words :
            if word * 2 not in text :
                text = text.replace(word, " ")
        if not text.strip() :
            answer += 1
    
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))