# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다. 
# 그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳의 빈도수를 업데이트 한다.
# a -> 0번째 인덱스 값을 올리고, z가 나왔다면 가장 마지막인 25번째 인덱스의 값을 추가해라.

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): #얘가 알파벳인지 검사하고
            continue
        arr_index = ord(char) - ord('a') #해당 문자를 인덱스로 치환한다. a -> 0, b -> 1 
        alphabet_occurrence_array[arr_index] += 1  # 빈도수 배열에 인덱스로 찾아가서 해당 값을 추가해준다.

    max_occurence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)): # 0, 1, 2 ...25
        alphabet_ccurence = alphabet_occurrence_array[index]

        if alphabet_ccurence > max_occurence:
            max_occurence = alphabet_ccurence
            max_alphabet_index = index
            # 8 -> i 인덱스 -> 아스키코드 형태로 만들고 -> 알파벳
    
    return chr(max_alphabet_index + ord('a'))




print(find_max_occurred_alphabet("hello my name is dingcodingco"))
