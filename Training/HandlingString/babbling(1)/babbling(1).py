def solution(babbling) :
    words = ['aya', 'ye', 'woo', 'ma']
    result = 0
    for text in babbling :
        for word in  words:
            text = text.replace(word, " ")
        if not text.strip(): #text.strip() is not an empty string -> True
            result += 1

    return result

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))