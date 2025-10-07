# 버블 정렬

# Swap 하는 법
# >>> a = 3
# >>> b = 4
# >>> a, b = b, a
# >>> print(a)
# 4
# >>> print(b)
# 3
# ----------------------

#input = [4, 6, 2, 9, 1]

# 1. 
# -> -> -> -> 
# i = 0 -> 맨 처음 모든 배열을 다 보게 되는 인덱스
# j = 4 -> 그 모든 배열을 다 보는 과정에서 몇번을 비교하는지의 횟수를 나타내주는 변수
# 0  1  2  3  4 
#[4, 6, 2, 9, 1]

# 2.
# i = 1
# j = 3
# 0  1  2  3  
#[4, 6, 2, 9, 1]

# 3.
# i = 2
# j = 2
# 0  1  2    
#[4, 6, 2, 9, 1]

# 4. 
# i = 3
# j = 1
# 0  1      
#[4, 6, 2, 9, 1]

# for i in range(5 - 1):
#   for j in range(5 - i - 1):
#       print(j)


input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))