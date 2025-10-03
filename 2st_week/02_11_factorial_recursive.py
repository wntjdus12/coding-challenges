# 재귀함수 - 팩토리얼 : 재귀함수는 탈출조건이 가장 중요!
# 3! = 3 * 2 * 1 

# factorial(n) = n * factorial(n - 1)
# factorial(n-1) = (n - 1) * factorial(n -2)
# ...
# factorial(1) = 1

def factorial(n):
    if n == 1:    #탈출 조건
        return 1

    return n * factorial(n - 1)

# 5*4*3*2*1 = 120
print(factorial(5))
