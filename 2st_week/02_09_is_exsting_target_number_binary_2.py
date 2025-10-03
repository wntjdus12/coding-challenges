#무작위 수 찾기
#무작위로 되어 있는 배열에서는 이진 탐색을 사용할 수가 없습니다.
# sort를 사용해서 정렬하고 이진 탐색을 해야합니다. 

# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

finding_target = 9
finding_numbers = [0, 3, 4, 5, 1 ,2, 4]

def is_exist_target_number_binary(target, array):
    array.sort() # 제자리 정렬 
    print(array)

    current_min = 0 
    currnet_max = len(array) - 1
    current_guess = (current_min + currnet_max) // 2

    while current_min <= currnet_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1 
        else:
            currnet_max = current_guess - 1

        current_guess = (current_min + currnet_max) // 2
    
    return False 

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
