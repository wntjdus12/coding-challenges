# 재귀 함수 : 재귀함수를 만들려면 항상 탈출 조건을 걸어줘야한다. 안 그러면 자기가 자기를 무한정 호출해버리기 떄문에
def count_down(number):
    if number < 0:
        return 

    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)