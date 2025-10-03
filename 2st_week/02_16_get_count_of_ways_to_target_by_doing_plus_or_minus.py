numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array): # 5까지 도달했을때 # 탈출조건
            all_ways.append(current_sum) # 여기에 삽입 
            return
        print("current is ", current_index, current_sum) # 3번째로 출력
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1 , current_sum + array[current_index]) #2번째 호출 한 다음에 다시 위로
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1 , current_sum - array[current_index]) 

    
    get_all_ways_by_doing_plus_or_minus(array, 0, 0) # 먼저 호출
    print("all_ways is ", all_ways)

    target_count = 0 

    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!