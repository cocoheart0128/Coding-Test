def solution(babbling):
    def check_word(bab):
        words = ["aya", "ye", "woo", "ma"]
        for word in words:
            if word in bab:
                bab = bab.replace(word,',')
            else:
                bab = bab
        if bab.replace(',','')=='':
            return 1
        else:
            return 0
    answer = 0
    for bab in babbling:
        v=check_word(bab)
        answer+=v
    
    return answer