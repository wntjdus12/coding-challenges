# 최대로 할인 적용하기

# 1500000 * 40% 금액
# 30000 * 20% 금액
# 2000 원가 -> 쿠폰의 개수만큼 prices를 전부 할인한 이후에 나머지 prices들은 원가로 계산해줘야 함

#   p_i
# [30000, 2000, 1500000]
#  c_i
# [20, 40]

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True) # 내림차순 정렬
    coupons.sort(reverse=True) # 내림차순 정렬

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0
    while price_index < len(prices) and coupon_index < len(coupons): #현재 가격과 쿠폰이 모두 배열 내의 원소일때
        discounted_price = prices[price_index] * (100 - coupons[coupon_index]) / 100 # 할인이 적용된 가격
        max_discounted_price += discounted_price
        price_index += 1 
        coupon_index += 1

    while price_index < len(prices): # 즉, 현재 price_index가 prices 길이 범위 내라면
        max_discounted_price += prices[price_index]
        price_index += 1
    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))