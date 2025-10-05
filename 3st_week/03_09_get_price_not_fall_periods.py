# 큐 문제 - 주식 가격 : 인덱스 관점에서 풀기

# i = 0
# j = 1
#   v v v v 
# 0 1 2 3 4 

# i = 1
# j = 2
#     v v v 
# 0 1 2 3 4 

# i = 2
# j = 3
#       v v 
# 0 1 2 3 4  

# i = 3
# j = 4
#         v 
# 0 1 2 3 4 

# 인덱스 
# 1234
# 234
# 34
# 4  

#  0  1  2  3  
# [1, 2, 3, 2, 3] 

# for i in range(0, 4, 1):
#     for j in range(i + 1 , 5, 1):
#         print(i , j)
 
prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    result = [0] * len(prices)

    for i in range(0, len(prices) - 1, 1):
        price_not_fall_period = 0 # 값이 얼마나 안떨어졌는지 알려주는 변수
        for j in range(i + 1 , len(prices), 1):
            if prices[i] <= prices[j]:
                price_not_fall_period += 1
            else: 
                price_not_fall_period += 1 # 가격이 떨어진 순간까지도 1초를 추가한 것으로 치겠다.
                break
        result[i] = price_not_fall_period
        print(i , j)

    return result
    


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))