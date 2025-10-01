input = 20

#소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
def find_prime_list_under_number(number):
    prime_list = []

    #2~20까지 찾아서 이것들이 소수인가? 소수라면 prime_list에 넣어라
    for n in range(2, number + 1): #2~n 까지의 숫자들이 n에 들어가는 것을 반복하라.
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else: 
            prime_list.append(n)

    return prime_list
    


result = find_prime_list_under_number(input)
print(result)