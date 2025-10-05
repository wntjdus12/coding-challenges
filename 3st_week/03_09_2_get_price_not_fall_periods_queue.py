# 큐 문제 - 주식 가격 : 큐 관점에서 풀기


# queue = deque()
# queue.append(3) [3]
# queue.append(4) [3] -> [4]
# queue.popleft() # 3이 반환되며 head, tail의 값은 [4]가 된다. 

from collections import deque


prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    result = []
    prices_queue = deque(prices) # 배열을 큐로 만듬 

    while prices_queue: # prices_queue가 비어있지 않다면 계속 반복한다. 
        price_not_fall_period = 0

        current_price = prices_queue.popleft() # [2, 3, 2, 3] # 앞에 있는 숫자들을 하나하나 뽑을거다
        for next_price in prices_queue:
            if current_price <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)

    return result
    


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))