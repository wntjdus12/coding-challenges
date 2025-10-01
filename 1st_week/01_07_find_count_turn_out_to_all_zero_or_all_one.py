input = "011110"

#0에서 1을 마주쳤을 때 뒤집는다 -> 전체를 0으로 만들기 위한 작업
#1에서 0을 마주쳤을 때 뒤집는다 -> 전체를 1로 만들기 위한 작업 


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0 # 모든 것을 0으로 만드는 최소 횟수 
    count_to_all_one = 0 # 모든 것을 1로 만드는 최소 횟수

    if string[0] == '0':
        count_to_all_one += 1 
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)