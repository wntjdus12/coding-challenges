# 해쉬 함수 - 링크드 리스트를 활용한 개선된 방법(체이닝 기법)

dict = {"fast": "삐른"}

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append(key, value) # ["333", 7] -> ["77", 6]

    def get(self, key): # 링크드 리스트에서 key값을 통해 해당하는 value 찾는 과정 
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()

linked_tuple.add("333", 7)
linked_tuple.add("77", 6)

print(linked_tuple.items)

print(linked_tuple.get("333"))



class LinkedDict:
    def __init__ (self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)  
        self.items[index].add(key, value) # index 번째의 LinkedTuple [(key, value)]
                                          # 한번 더 호출되면?
                                          # index 번째의 LinkedTuple [(key, value), (key2, value2)]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key) # LinkedTuple [(key, value), (key2, value2)]

my_dict = Dict()
my_dict.put("test", 3)
my_dict.put("333", 7)
my_dict.put("77", 6)

# 333이랑 77의 키값 인덱스가 1로 동일한 경우에는 이렇게 키값과 value를 동시에 저장할 수 있는 링크드 리스트를 만들어야 한다.
# self.items[1] = ["333", 7] -> ["77", 6] 

# print(my_dict.get("333")) # 333의 value를 구하려고 한다면 
# 1. hash("333") % len(self.items) -> index가 1이 나온다.
# 2. self.items[1] -> ["333", 7] -> ["77", 6]
# 3. ["333", 7]에 있네! 그럼 value는 7이야!