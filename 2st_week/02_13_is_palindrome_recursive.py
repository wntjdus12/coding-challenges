#재귀함수 : 재귀적 회문검사
# 재귀함수는 문제의 범위를 조금씩 좁혀나가는 거예요.

# count_down 60 -> 59 -> 58 ...
# factorial(n) -> factorial(n-1) -> factorial(1)

# abcba
# bcb

#소주만병만주소
#주만병만주

input = "abcba"


def is_palindrome(string): #소주만병만주소
    if string[0] != string[-1]: #탈출조건 #맨첫번째랑 맨마지막 비교 
        return False
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1]) # 주만병만주 / string의 1번째 인덱스부터 -1번째 인덱스까지 문자열을 자르겠다.


print(is_palindrome(input))