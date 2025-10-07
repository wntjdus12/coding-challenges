# 병합 정렬 - 재귀 함수

# MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))

# merge_sort([5, 3, 2, 1, 6, 8, 7, 4])

# left_array = merge_sort([5, 3, 2, 1])
#              merge_sort([5, 3])
#                     left_array = merge_sort([5])
#                     right_array = merge_sort([3])
#                     merge(left_array, right_array) = [3, 5]
#              merge_sort([2, 1])

# right_array = merge_sort([6, 8, 7, 4])

array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    if len(array) <= 1: # 탈출 조건(재귀함수는 탈출조건 필수) : 만약 배열의 길이가 1보다 같거나 작다면 그냥 배열 반환해라
        return array

    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    print(left_array, right_array)

    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1 
        else:
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1 

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))