# 해쉬 함수

# put(key, value) -> dictionary 에 key 해당하는 곳에 value를 저장해두겠다.
# get(key) -> dictionary에 key 해당하는 value를 반환해라.

# 하지만
# a b c d e ... z -> 26개인데
# [0, 1, 2, ... , 8] -> 8개이니까요 -> 충돌발생
# 1. Chaning 기법 : 충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리한다. 

dict = {"fast": "삐른"}

class Dict:
    def __init__ (self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)  # 키값을 items의 길이만큼 나누고 그 값을 인덱스로 사용
        self.items[index] = value # 그 items의 인덱스에 value를 넣어두겠다.

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))