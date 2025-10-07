# 피보나치 수열 - 동적 계획법 -> 문제를 쪼갤 수 있는 구조 일때만 사용 가능. 
# 즉, 겹치는 부분 문제가 감지되는 상황에서만 !!!
# Q. 피보나치 수열의 100번째 수를 구하시오.

input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# 1. 메모에 이미 해당 값이 있으면 반환한다.
# 2. 만약 없다면, 그 값을 피보나치를 통해 구하고 메모에 저장한다.


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo



print(fibo_dynamic_programming(input, memo))