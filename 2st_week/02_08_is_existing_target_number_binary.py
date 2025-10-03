# 이진 탐색 => 이진 탐색을 하기 위한 가장 강력한 전제 조건은 이 숫자들이 정렬이 되어있어야 한다는 것 

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0  #최솟값
    current_max = len(array) - 1 #최댓값
    current_guess = (current_min + current_max) // 2  #탐색값

    while current_min <= current_max:
        if array[current_guess] == target: # 정답!
            return True
        elif array[current_guess] < target: #UP!
            current_min = current_guess + 1
        else: #array[current_guess] > target:   #DOWN~
            current_max = current_guess - 1 

        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

# UP -> [9, 10, 11, 12, 13, 14, 15, 16]
# DOWN -> [1, 2, 3, 4, 5, 6, 7]