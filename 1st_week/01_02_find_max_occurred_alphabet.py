#1. a,b,c 처럼 문자가 해당 문자얄에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 그 알파벳으로 변환한다.
# a -> hello my name is dingcodingco -> 0 max_occurence = 0 , max_alphabet = a
# b -> hello my name is dingcodingco -> 0 max_occurence = 0 , max_alphabet = b
# c -> hello my name is dingcodingco -> 2 max_occurence = 2 , max_alphabet = c
# d -> hello my name is dingcodingco -> 2 max_occurence = 2 , max_alphabet = d


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o", "p", "q", "r", "s", "t", "u", "v" "w", "x", "y", "z"]
    
    max_occurence = 0
    max_alphabet = alphabet_array[0] #a

    for alphabet in alphabet_array:
        occurence = 0

        for char in string:
            if char == alphabet:
                occurence += 1 
        
        if occurence > max_occurence:
            max_alphabet = alphabet
            max_occurence = occurence

    return max_alphabet, max_occurence



result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
