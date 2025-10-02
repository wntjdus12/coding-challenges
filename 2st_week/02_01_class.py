class Person: 
    def __init__(self, name_param): # 생성자
        self.name = name_param
        print("hihi i am created", self, self.name)

    def talk(self): # 메서드 
        print("안녕하세요 저는 ", self.name, "입니다.")


person_1 = Person("주서연")
person_1.talk()