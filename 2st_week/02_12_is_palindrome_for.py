# 재귀함수 : 반복문을 사용한 회문검사
# Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오. 
# "abcba" -> True 

input = "abcba"

# v   v
#  v v
#   v
# abcba


def is_palindrome(string):
    n = len(string)
    for i in range(n): # i : 0 ~ n-1 
        if string[i] != string[n - 1 - i]:
            return False
    return True


print(is_palindrome(input))