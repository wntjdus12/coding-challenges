# 이진 탐색 => 특정 문자열이 배열에 존재하는지만 확인하면 됨
# 정렬을 할 필요 없이 집합 자료형이라는 것 사용
# 집합 : 중복을 허용하지 않는 자료형 

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)