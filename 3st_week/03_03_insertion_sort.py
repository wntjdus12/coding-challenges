# 삽입 정렬

#     1
# [4, 6, 2, 9, 1]

#     1  2
# [4, 6, 2, 9, 1]

# 1 -> 2, 1 -> 3, 2, 1 -> 

# for i in range(1, 5):
#     for j in range(i):
#         i - j -> 인덱스 값
#         i = 1 j = 0 -> 1 
#         i = 2 j = 0 -> 2
#         i = 2 j = 1 -> 1
#         

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else: 
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))