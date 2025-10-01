# 빅오 -> 최악의 경우.
# 빅오메가 -> 최선의 경우.


def is_number_exist(number, array):
    for element in array:      # array의 길이만큼 아래 연산이 실행
        if number == element:    # 비교 연산 1번 실행
            return True          # 시간복잡도 N 만큼 걸린다.
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))


# 1.입력값에 비례해서 얼마나 연산량이 늘어날 것인지를 파악하는 것이 중요. 1? N? N제곱?
# 2. 공간 복잡도 보다는 시간 복잡도를 더 줄이기 위해 고민  
# 3. 최악의 경우에 시간이 얼마나 소요될지(빅오 표기법)에 대해 고민하자.
